from datetime import date
from random import sample, choice, randint, uniform
from django.db import IntegrityError
from .models import Game


title_words = ["Céu", "Ventura", "Eclipse", "Sombra", "Aventura", "Mistério", "Lenda", "Luz", "Desafio", "Labirinto", "Espírito", "Epic", "Obsidiana", "Ressonância", "Horizonte", "Abyss", "Fórmula", "Névoa", "Vortex", "Crepúsculo", "Catalyst", "Quasar", "Pandemônio", "Aurora", "Lâmina", "Reflexo", "Circuito", "Êxodo", "Chronos", "Vigília", "Neon", "Oráculo", "Nebulosa", "Caverna", "Legado", "Harbinger", "Renegado", "Nexus", "Fronteira", "Serpente", "Ascensão", "Sinfonia", "Voraz", "Galáxia", "Espectro", "Silhueta", "Áurea", "Miragem", "Eon", "Inferno", "Quimera", "Ecos", "Crepitação", "Zenith", "Crânio", "Ruptura", "Estrondo", "Zephyr", "Mirage", "Quasar", "Apex", "Abyssal", "Vorpal", "Ignição", "Croma", "Apoteose", "Penumbras", "Êxtase", "Marauder", "Equinócio", "Aegis", "Veredicto", "Nox", "Lunático", "Saudade", "Aurora", "Perigoso", "Pioneiro", "Aventura", "Online", "Quest", "Puzzle" "Desafio", "Mistério", "Exploração", "Épico", "Lenda", "Fantasia", "Sombra", "Labirinto", "Céu", "Abismo", "Cronos", "Vortex", "Eterno", "Névoa", "Vingança", "Luminar", "Abyss", "Renegado", "Caos", "Nebulosa", "Fúria", "Ruptura", "Ascensão", "Estelar", "Voraz", "Imortal", "Quasar", "Crepúsculo", "Inferno", "Vórtice", "Enigma", "Serpente", "Astral", "Sussurro", "Eclipse", "Espectro", "Magma", "Ruína", "Néon", "Crepúsculo", "Obsidiana", "Apex", "Fênix", "Terraço", "Aurora", "Aegis", "Vórtice", "Ígneo", "Oráculo", "Eon", "Cósmico", "Pulsar", "Serpentex", "Açoite", "Esplendor", "Núcleo", "Tempestade", "Helix", "Valente", "Arauto", "Silente", "Coração", "Liberdade", "Amparo", "Exílio", "Ícaro", "Eclético", "Xanadu", "Savana", "Zênite", "Utopia", "Abissal", "Nimbus", "Dédalo", "Fórum", "Quimera", "Pandora", "Záfiro"]
developer_name = ["PixelForge Jogos", "Infinite Realms Entertainment", "QuantumByte Studios", "Nebula Dynamics", "MysticPulse Interactive", "EchoSphere Jogos", "Enigma Nexus Creations", "Celestial Horizon Studios", "Vortex Interactive", "DreamForge Gaming", "ChronoBit Studios", "NovaVerse Creations", "EtherSpark Jogos", "Galactic Pulse Studios", "Cyberscape Innovations", "OmniRealm Studios", "Horizon Forge Interactive", "AetherByte Jogos", "CosmosCraft Studios", "Nebula Odyssey Creations", "Immersive Realities Co.", "NebulaNova Jogos", "Quantum Nexus Interactive", "SolarFlare Studios", "HyperDream Interactive", "WarpZone Innovations", "AstralPulse Jogos", "QuantumLeap Creations", "CelestialSpark Studios", "StarVoyage Jogos", "TimeShift Interactive", "DarkMatter Creations", "ElementalForge Jogos", "VirtualPulse Studios", "Etherial Realms Entertainment", "EnchantedBit Jogos", "AstroByte Innovations", "NebulaCraft Studios", "TechnoRealm Jogos", "TimeWarp Interactive", "MythosForge Studios", "WarpDrive Jogos", "Infinite Realities Co.", "QuantumQuasar Creations", "StarlightPulse Jogos", "EchoCraft Studios", "CosmicDream Interactive", "WarpGate Jogos", "EtherealEdge Studios", "NebulaQuest Creations", "QuantumSculpt Jogos", "InfinityPulse Studios", "MysticArcade Innovations", "DreamWeave Jogos", "NebulaRift Studios", "ElementalPulse Jogos", "TimelessForge Creations", "QuantumVortex Interactive", "NovaCraft Studios", "SolarSculpt Jogos", "WarpStorm Innovations", "EtherVoyage Studios", "CelestialCraft Jogos", "NebulaSpectra Creations", "QuantumFlux Interactive", "MysticChronicle Studios", "HyperNova Jogos", "WarpRealm Innovations", "StellarCraft Studios", "TimeQuake Jogos", "EtherLink Interactive", "CelestialSculpt Studios", "QuantumFusion Jogos", "NebulaSphere Creations", "EnchantByte Studios", "StarForge Jogos", "TechnoVortex Interactive", "NovaPixel Studios", "ElementalEdge Jogos", "MysticWave Creations"]
genres = ["Ação", "Arcade", "Jogo de Ritmo", "Hack and Slash", "Luta e Artes Marciais", "Plataforma", "Endless Running", "Shoot 'em Up", "Beat 'em Up", "Tiro em Primeira Pessoa", "Tiro em Terceira Pessoa", "Aventura", "Casuais", "Metroidvania", "Objetos Escondidos", "Quebra-Cabeça", "Romance Visual", "Trana Excepcional", "RPG", "JRPGs", "RPGs de Aventura", "RPGs de Ação", "RPGs de Estratégia", "RPGs em Grupos", "RPGs em Turnos", "Roguelike", "Simulação", "Contrução e Automação", "Empregos e Passatempos", "Encontros", "Espaço", "Aviação", "Física", "Faça o que Quiser", "Rural", "Fabricação", "Simulação de Vida", "Imersivo", "Estratégia", "Cidades e Colônuas", "Defesa de Torres", "Estratégia Baseada em Turnos", "Estratégia em Tempo Real", "Grande Estratégia e 4x", "Militar", "Jogo de Tabuleiro", "Jogo de Cartas", "Esporte", "Corrida", "Esporte em Equipe", "Esportes Individuais", "Pescaria", "Caça", "Simuladores Automobilísticos", "Simuladores de Esporte", "Anime", "Espaciais", "Ficção Científica", "Cyberpunk", "Mistério", "Investigação", "Mundo Aberto", "Sobrevivência", "Somente Adultos", "Terror", "Competitivo On-line", "Cooperativo", "MMO", "Multijogador", "Multijogador Local e em Grupo", "Rede Local", "Um jogador"]

def generate_random_games(num_games=1):
    random_games = []

    for _ in range(num_games):
        word1, word2 = sample(title_words, 2)
        name = f"{word1} {word2}"
        developer = choice(developer_name)
        genre = choice(genres)
        release_date = date(randint(2000, 2023), randint(1, 12), randint(1, 28))
        price = round(uniform(0, 300), 2)

        game_instance = Game(name=name, developer=developer, genre=genre, release_date=release_date, price=price)

        try:
            game_instance.save()
            random_games.append(game_instance)
        except IntegrityError as e:
            print(f"Error saving game: {e}")

    return random_games