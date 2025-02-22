let allPokemons = [];
let offset = 20;
const limit = 20;
let isLoading = false;

const searchInput = document.getElementById('search');
const pokemonContainer = document.getElementById('pokemon-container');
const loadMoreButton = document.getElementById('load-more');

const pokemonsIniciais = [
    'bulbasaur', 'pikachu', 'charizard', 'squirtle', 'eevee', 'charmander', 'ivysaur', 'charmeleon', 
    'wartortle', 'caterpie', 'metapod', 'butterfree', 'blastoise', 'pidgey', 'kakuna', 'spearow', 
    'clefairy', 'vulpix', 'arbok', 'raticate', 'ekans', 'beedrill', 'clefable', 'rhyhorn', 'tangela',
    'jigglypuff', 'wigglytuff', 'machop', 'machoke', 'machamp', 'bellossom', 'mankey', 'primeape', 
    'diglett', 'dugtrio', 'zubat', 'golbat', 'psyduck', 'golduck', 'sandshrew', 'poliwag', 'magnemite',
    'venusaur', 'growlithe', 'poliwhirl', 'kadabra', 'tentacool', 'geodude', 'ponyta'
];

async function carregarPokemonsIniciais() {
    isLoading = true;
    let initialPokemons = pokemonsIniciais.slice(0, 20); // Carrega somente os 20 primeiros Pokémon
    for (let pokemon of initialPokemons) {
        const data = await getPokemonData(pokemon);
        if (data) {
            allPokemons.push(data);
        }
    }

    // Ordena os Pokémon por número da Pokédex antes de exibir
    allPokemons.sort((a, b) => a.id - b.id);
    
    // Exibe os Pokémon na tela
    allPokemons.forEach(displayPokemon);
    offset = 20; // Ajusta o offset para iniciar após os 20 primeiros
    isLoading = false;
}

async function getPokemonData(pokemonName) {    
    try {
        const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemonName.toLowerCase()}`);
        if (!response.ok) throw new Error('Pokémon não encontrado');
        const data = await response.json();

        const speciesData = await fetch(data.species.url).then(res => res.json());
        const evolutions = await getEvolutions(speciesData.evolution_chain.url);

        data.evolutions = evolutions;
        return data;
    } catch (error) {
        console.error(error);
        return null;
    }
}

async function getEvolutions(evolutionChainUrl) {
    try {
        const response = await fetch(evolutionChainUrl);
        const data = await response.json();
        const evolutions = [];

        let currentEvolution = data.chain;
        while (currentEvolution) {
            const pokemonName = currentEvolution.species.name;
            
            // Buscar os dados completos do Pokémon para pegar a imagem
            const pokemonResponse = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemonName}`);
            const pokemonData = await pokemonResponse.json();
            
            evolutions.push({
                name: pokemonName,
                image: pokemonData.sprites.front_default, // Pega a imagem frontal padrão
            });

            currentEvolution = currentEvolution.evolves_to[0]; // Passa para a próxima evolução
        }

        return evolutions;
    } catch (error) {
        console.error("Erro ao buscar evoluções:", error);
        return [];
    }
}

function displayPokemon(pokemon) {
    const card = document.createElement('div');
    card.classList.add('pokemon-card');

    pokemon.types.forEach(type => {
        card.classList.add(`type-${type.type.name.toLowerCase()}`);
    });

    const weaknesses = getWeaknesses(pokemon.types.map(type => type.type.name));

    card.innerHTML = `
        <img src="${pokemon.sprites.front_default}" alt="${pokemon.name}">
        <p>nº ${String(pokemon.id).padStart(4, '0')}</p>
        <h3>${pokemon.name}</h3>
        <p><strong>Tipo:</strong> ${pokemon.types.map(type => type.type.name).join(', ')}</p>
        <p><strong>Fraquezas:</strong> ${weaknesses.join(', ') || 'Nenhuma'}</p>
    `;

    card.addEventListener('click', () => showPokemonDetails(pokemon));
    pokemonContainer.appendChild(card);
}

function displayPokemonDetails(pokemon) {
    const modalContent = document.querySelector(".modal-content");
    modalContent.innerHTML = `
        <h2>${pokemon.name}</h2>
        <img src="${pokemon.image}" alt="${pokemon.name}">
        
        <div class="pokemon-stats">
            ${pokemon.stats.map(stat => `
                <p>${stat.name.toUpperCase()}: <span class="stat-value">${stat.value}</span></p>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: ${stat.value}%;"></div>
                </div>
            `).join("")}
        </div>
    `;

    document.querySelector(".modal").style.display = "block";
}

async function showPokemonDetails(pokemon) {
    const modal = document.createElement('div');
    modal.classList.add('modal');
    
    // Função para definir a cor da barra de progresso
    function getStatColor(value) {
        const percent = value / 255; // Considerando 255 como valor máximo base
        const r = Math.round(255 * percent);
        const g = Math.round(255 * (1 - percent));
        return `rgb(${r}, ${g}, 0)`;
    }

    // Buscar imagens das evoluções, se necessário
let evolutionImages = [];

try {
    if (pokemon.evolutions && pokemon.evolutions.length > 0 && typeof pokemon.evolutions[0] === "string") {
        evolutionImages = await getEvolutionImages(pokemon.evolutions);
    } else {
        evolutionImages = pokemon.evolutions || []; // Evita que seja undefined
    }
} catch (error) {
    console.error("Erro ao buscar imagens das evoluções:", error);
    evolutionImages = []; // Define um array vazio para evitar problemas no restante do código
}
    
modal.innerHTML = `
<div class="modal-content">
    <span class="close-button">&times;</span>
    <img src="${pokemon.sprites.front_default}" alt="${pokemon.name}">
    <h2>${pokemon.name} (nº${pokemon.id.toString().padStart(4, '0')})</h2>
    <p><strong>Tipo:</strong> ${pokemon.types.map(type => type.type.name).join(', ')}</p>
    <p><strong>Altura:</strong> ${pokemon.height / 10}m</p>
    <p><strong>Peso:</strong> ${pokemon.weight / 10}kg</p>

    <h3>Estatísticas:</h3>
    <div class="pokemon-stats">
        ${pokemon.stats.map(stat => `
            <div class="stat">
                <span>${stat.stat.name.toUpperCase()}: ${stat.base_stat}</span>
                <div class="progress-bar" style="width: ${stat.base_stat / 2.55}%; background-color: ${getStatColor(stat.base_stat)}"></div>
            </div>
        `).join('')}
    </div>

    <h3>Evoluções:</h3>
    <div class="evolutions">
        ${pokemon.evolutions && pokemon.evolutions.length > 0 ? 
            pokemon.evolutions.map(evolution => `
                <div class="evolution">
                    <h5>${evolution.name}</h5>  
                    <img src="${evolution.image}" alt="${evolution.name}">
                </div>
            `).join('') : '<p>Nenhuma</p>'
        }
    </div>
</div>
`;

    document.body.appendChild(modal);

    // Fechar modal ao clicar no botão X
    modal.querySelector(".close-button").addEventListener("click", () => modal.remove());

    // Fechar modal ao clicar fora dela
    modal.addEventListener("click", (e) => {
        if (e.target === modal) modal.remove();
    });
}

function getWeaknesses(types) {
    const typeWeaknesses = {
        normal: ["fighting"], fire: ["water", "rock", "ground"], water: ["electric", "grass"],
        electric: ["ground"], grass: ["fire", "ice", "poison", "flying", "bug"], ice: ["fire", "fighting", "rock", "steel"],
        fighting: ["flying", "psychic", "fairy"], poison: ["ground", "psychic"], ground: ["water", "grass", "ice"],
        flying: ["electric", "ice", "rock"], psychic: ["bug", "ghost", "dark"], bug: ["fire", "flying", "rock"],
        rock: ["water", "grass", "fighting", "ground", "steel"], ghost: ["ghost", "dark"], dragon: ["ice", "dragon", "fairy"],
        dark: ["fighting", "bug", "fairy"], steel: ["fire", "fighting", "ground"], fairy: ["poison", "steel"]
    };

    let weaknesses = [];
    types.forEach(type => {
        if (typeWeaknesses[type]) {
            weaknesses = [...weaknesses, ...typeWeaknesses[type]];
        }
    });
    return [...new Set(weaknesses)].slice(0, 2);
}

async function carregarMaisPokemons() {
    if (isLoading) return;
    isLoading = true;

    let newPokemons = [];
    for (let i = offset; i < offset + limit; i++) {
        if (pokemonsIniciais[i]) {
            const data = await getPokemonData(pokemonsIniciais[i]);
            if (data) {
                newPokemons.push(data);
            }
        }
    }

    // Ordena antes de exibir para evitar exibição fora de ordem
    newPokemons.sort((a, b) => a.id - b.id);

    // Adiciona ao array principal
    allPokemons.push(...newPokemons);
    allPokemons.sort((a, b) => a.id - b.id); // Garante a ordenação geral

    // Atualiza a exibição
    atualizarListaPokemon(); 

    offset += limit;

    if (offset>=pokemonsIniciais.length) {
        loadMoreButton.style.display = 'none';
    }

    isLoading = false;
}

// Função para atualizar a exibição
function atualizarListaPokemon() {
    const pokemonContainer = document.getElementById("pokemon-container");
    pokemonContainer.innerHTML = ""; // Limpa antes de adicionar
    allPokemons.forEach(displayPokemon);
}

    function searchPokemon() {
        const query = searchInput.value.trim().toLowerCase();
        pokemonContainer.innerHTML = '';

        const filteredPokemons = allPokemons.filter(pokemon => 
            pokemon.name.includes(query) ||
            String(pokemon.id) === (query) ||
            String(pokemon.id).padStart(2, '0') === (query) ||
            String(pokemon.id).padStart(3, '0') === (query) ||
            String(pokemon.id).padStart(4, '0') === (query) // Permite busca pelo número formatado (ex: 0001)
        );

        // Ordena os Pokémons filtrados por número
        filteredPokemons.sort((a, b) => a.id - b.id);
        filteredPokemons.forEach(displayPokemon);
    }

    searchInput.addEventListener('input', searchPokemon);
    loadMoreButton.addEventListener("click", carregarMaisPokemons);
    window.onload = carregarPokemonsIniciais;

    // Evento para expandir os cards ao clicar
    document.querySelectorAll('.pokemon-card').forEach(card => {
        card.addEventListener('click', function () {
        this.classList.toggle('pokemon-card-expanded');
        });
    });