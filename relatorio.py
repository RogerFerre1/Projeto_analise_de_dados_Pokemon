from fpdf import FPDF

class PDF(FPDF):

    def titulo(self, label):
        self.set_font('helvetica', 'B', size=24)
        self.cell(0, 60, label, 0, 1, 'C')

    def sub_titulo(self, label):
        self.set_font('helvetica', 'I', size=16)
        self.cell(0, 10, label, 0, 1, 'C')

    def linha_centralizada(self, label):
        self.set_font('helvetica', '', size=12)
        self.cell(0, 10, label, 0, 1, 'C')

    def titulo_base(self, label):
        self.set_font('helvetica', 'B', size=16)
        self.cell(0, 6, label, 0, 1, 'L')
        self.ln()

    def subtitulo_base(self, label):
        self.set_font('helvetica', 'B', size=14)
        self.cell(0, 4, label, 0, 1, 'L')
        self.ln()

    def sub_subtitulo_base(self, label):
        self.set_font('helvetica', 'B', size=12)
        self.cell(0, 6, label, 0, 1, 'L')
        self.ln()

    def paragrafo(self, text):
        self.set_font('helvetica', 'B', size=11)
        self.multi_cell(0, 7, text)
        self.ln()

    def imagem(self, img, x, y, w):
        self.image(img, x, y, w)

    def adicionar_sumario(self, titulo, nivel=1):
        tab = "    " * (nivel - 1)
        self.cell(0, 10, f"{tab}{titulo}", ln=True)

pdf = PDF()

# Pág 1
pdf.add_page()

pdf.titulo('Análise de dados')
pdf.sub_titulo('POKÉMON: ANÁLISE ESTATÍSTICA')
pdf.image('pokemon_relat.jpg', 40, 90, 130)
pdf.ln(160)
pdf.linha_centralizada('Autor: Roger Ferreira de Souza')    

# Pág 2
pdf.add_page()

pdf.adicionar_sumario('1. Introdução', nivel=1)
pdf.adicionar_sumario('2. Análise dos dados', nivel=1)
pdf.adicionar_sumario('2.1 Distribuição Percentual de Pokémon por Categoria de Tipo', nivel=2)
pdf.adicionar_sumario('2.2 Análise da Ocorrência de Tipos Secundários em Pokémon', nivel=2)
pdf.adicionar_sumario('2.3 Comparativo da Distribuição de Pokémon Lendários por Geração', nivel=2)
pdf.adicionar_sumario('2.4 Distribuição dos Valores Médios de Stats Base por Tipo', nivel=2)
pdf.adicionar_sumario('2.4.1 Tipos com maior HP', nivel=3)
pdf.adicionar_sumario('2.4.2 Tipos com maior Attack', nivel=3)
pdf.adicionar_sumario('2.4.3 Tipos com maior Defense', nivel=3)
pdf.adicionar_sumario('2.4.4 Tipos com maior Special Attack', nivel=3)
pdf.adicionar_sumario('2.4.5 Tipos com maior Special Defense', nivel=3)
pdf.adicionar_sumario('2.4.6 Tipos com maior Speed', nivel=3)
pdf.adicionar_sumario('2.4.7 Tipos com maior Total de stats', nivel=3)
pdf.adicionar_sumario('2.5 Análise Comparativa das Gerações com Base nos Stats Totais', nivel=2)
pdf.adicionar_sumario('2.6 Identificação do Tipo Predominante em Cada Geração de Pokémon', nivel=2)
pdf.adicionar_sumario('3. Conclusão', nivel=1)

# Pág 3
pdf.add_page()

pdf.titulo_base('1. Introdução')
pdf.paragrafo('A franquia Pokémon transcendeu o status de simples marca de entretenimento para se tornar parte do imaginário cultural global. Com um valor estimado em mais de 100 bilhões de dólares, ela consolidou-se como a franquia mais valiosa do mundo, presente em múltiplas mídias como jogos, animes e mangás.')
pdf.paragrafo('Apesar dessa relevância, um aspecto central da série permanece pouco explorado: a Pokédex. Introduzida desde o primeiro jogo, sua função principal é catalogar informações sobre os Pokémon. Com o tempo, porém, passou a ser utilizada quase exclusivamente por jogadores competitivos ou fãs mais dedicados.')
pdf.paragrafo('Este estudo tem como objetivo analisar a Pokédex sob uma perspectiva quantitativa, investigando insights interessantes como a distribuição de status base e os tipos predominantes de cada geração,com o intuito de revelar tendências sobre design, ambientação e decisões criativas utilizadas nos jogos. Para isso, utilizamos dados disponibilizados no Kaggle, que oferecem uma visão detalhada das características de cada Pokémon.')

# Pág 4
pdf.add_page()

pdf.titulo_base('2. Análise dos dados')
pdf.subtitulo_base('2.1 Distribuição Percentual de Pokémon por Categoria de Tipo')
pdf.paragrafo('O gráfico de pizza mostra uma vantagem significativa na existência de Pokémon do tipo Água(12,54%) e do tipo Normal(11,18%) em relação ao total, uma causa disso pode se dar ao fato dos 2 tipos serem equilibrados em relação a outros, visto que o tipo Água possui poucas fraquezas(apenas Elétrico e Planta) e do tipo Normal ser um tipo neutro que não possui muitas vantagens e desvantagens, além de serem mais numerosos nas rotas iniciais, o que torna este tipo muito amigável para que jogadores iniciantes se acostumem com a mecânica do jogo, enquanto tipos mais raros como *Dragão* tornam-se alvos de desejo aumentando a emoção ao encontrar, capturar e treinar um deles.')
pdf.paragrafo('Por outro lado, tipos como Gelo(2,30%) e Fada(2,73%) são escassos intencionalmente com a mesma finalidade de manter o equilibrio, o caso do tipo Fada em particular se diferencia do tipo Gelo, pois ele foi introduzido tardiamente nos jogos para ser mais um counter do tipo Dragão, que, por conta de seu baixo número de fraquezas e seus altos stats por muito tempo dominou o game, contudo, os 2 tipos se mantiveram escassos para que o tipo Dragão não perdesse seu impacto na aventura.')
pdf.paragrafo('O tipo Voador(1,02%) tem baixa participação não por ser raro, mas por geralmente aparecer como tipagem secundária, o que o faz ocupar uma posição menor neste estudo baseado apenas nos tipos primários.')
pdf.image('graficos/1-Grafico_porcent_tipo_pkm.png', 10, 155, 200, 140)

# Pág 5
pdf.add_page()

pdf.subtitulo_base('2.2 Análise da Ocorrência de Tipos Secundários em Pokémon')
pdf.paragrafo('O gráfico de pizza compara a proporção de Pokémon com e sem tipo secundário. Observa-se que 53,79% possuem um tipo secundário, enquanto 46,21% têm apenas o tipo primário.')
pdf.paragrafo('Essa tendência indica que os designers priorizam combinações de tipos para aumentar a diversidade estratégica, tornando batalhas mais complexas e interessantes.')
pdf.paragrafo('Ao mesmo tempo,a presença significativa de Pokémon de tipo único garante uma base simples e equilibrada, útil para jogadores iniciantes formarem suas estratégias sem a necessidade de estudar a fundo o game e garantir sua diversão mesmo com pouco conhecimento.')
pdf.paragrafo('Essa distribuição evidencia o cuidado no design do jogo e na experiência do jogador, equilibrando diversidade, aprendizado e complexidade.')
pdf.image('graficos/2-Grafico_pkm_tipo_sec.png', 10, 135, 200)

# Pág 6
pdf.add_page()

pdf.subtitulo_base('2.3 Comparativo da Distribuição de Pokémon Lendários por Geração')
pdf.paragrafo('O gráfico de barras mostra a quantidade de Pokémon lendários de cada geração.')
pdf.paragrafo('Nota-se um crescimento constante da 1ª geração(5) até a 5ª geração(13), sugerindo uma estratégia de aumentar a diversidade e o apelo desses Pokémon ao longo dos anos. A partir da 6ª geração, entretanto, observa-se uma oscilação, com reduções e novos picos, indicando mudanças na filosofia de design e narrativa. A 9ª geração se destaca por apresentar apenas 2 lendários, possivelmente para reforçar a exclusividade desse grupo ou para priorizar novas mecânicas de jogo.')
pdf.paragrafo('Essa análise revela que a distribuição de lendários não segue uma progressão linear, mas sim reflete escolhas criativas e estratégicas de cada fase da franquia.')
pdf.image('graficos/3-Grafico_lend_gen.png', 10, 150, 200)

# Pág 7
pdf.add_page()

pdf.subtitulo_base('2.4 Distribuição dos Valores Médios de Stats Base por Tipo')
pdf.sub_subtitulo_base('2.4.1 Tipos com maior HP')
pdf.paragrafo('O gráfico de barras apresenta a média de HP dos Pokémon ordenadas por tipo. Observa-se que os tipos Dragão, Gelo e Normal possuem os maiores valores médios, indicando maior resistência e durabilidade em combate.')
pdf.paragrafo('Em constraste, Elétrico, Inseto e Fantasma apresentam menor HP médio, sugerindo que esses tipos compensam com habilidades ofensivas ou velocidade.')
pdf.paragrafo('Essa distribuição evidencia uma estratégia de balanceamento do jogo, na qual tipos duráveis oferecem resistência, enquanto tipos especializados oferecem outras vantagens, permitindo aos jogadores montar equipes diversificadas e estratégicas.')
pdf.image('graficos/4-1-Grafico_hp_tipo.png', 10, 150, 200)

# Pág 8
pdf.add_page()

pdf.sub_subtitulo_base('2.4.2 Tipos com maior Attack')
pdf.paragrafo('O gráfico de barras apresenta a média de Attack base dos Pokémon por tipo. Observa-se que os tipos Dragão, Lutador, Terrestre e Aço possuem os maiores valores médios, indicando uma maior capacidade ofensiva, com Pokémon desse tipo sendo capazes de causar mais danos físicos em combate.')
pdf.paragrafo('Em contraste, os tipos Elétrico, Fada, Inseto e Psíquico apresentam os menores valores de attack médio, sugerindo que esses tipos podem priorizar estratégias baseadas em habilidades especiais ou resistência, ao invés de dano massivo direto.')
pdf.paragrafo('Essa distribuição revela uma abordagem de balanceamento no design do jogo, onde tipos com ataques físicos fortes, como Dragão e Lutador, são mais eficazes em ataques rápidos e poderosos, enquanto tipos com ataques mais fracos, como Elétrico e Fada, podem se destacar em aspectos como controle de campo, velocidade, ataques especiais ou efeitos de status.')
pdf.image('graficos/4-2-Grafico_atk_tipo.png', 10, 150, 200)

# Pág 9
pdf.add_page()

pdf.sub_subtitulo_base('2.4.3 Tipos com maior Defense')
pdf.paragrafo('O gráfico de barras apresenta a média de Defense base dos Pokémon por tipo. Observa-se que os tipos Aço, Pedra e Terrestre possuem os maiores valores médios, indicando uma grande resistência e durabilidade em combate, esses tipos, com Defense acima de 100, são muito eficazes em absorver danos físicos, tornando-se ótimos para proteger a equipe.')
pdf.paragrafo('Em constraste, os tipos Normal, Elétrico e Voador apresentam as menores médias de Def, sugerindo uma maior vulnerabilidade a ataques diretos. Pokémon desses tipos podem compensar com alta velocidade ou habilidades especiais, priorizando ofensividade ou evasão em vez de resistência física.')
pdf.paragrafo('Essa distribuição demonstra uma estratégia de balanceamento do jogo, na qual tipos com alta Def se concentram em absorver muito os Ataques físicos e em fazer uma linha de frente para proteger o resto do time, enquanto os tipos com menor Def se concentram geralmente em oferecem um dano explosivo ou outras habilidades táticas contra outros treinadores.')
pdf.image('graficos/4-3-Grafico_def_tipo.png', 10, 150, 200)

# Pág 10
pdf.add_page()

pdf.sub_subtitulo_base('2.4.4 Tipos com maior Special Attack')
pdf.paragrafo('O gráfico de barras apresenta a média de Special Attack(Sp.Atk) base dos Pokémon por tipo. Observa-se que os tipos Psíquico, Dragão e Fogo possuem as maiores médias , indicando uma grande capacidade ofensiva por meio de ataques especiais. Pokémon desses tipos são particularmente poderosos em causar dano à distância, frequentemente com habilidades que envolvem manipulação de elementos ou poderes psíquicos.')
pdf.paragrafo('Em contraste, os tipos Normal, Lutador e Terrestre apresentam as menores médias de Sp.Atk, sugerindo que esses tipos são mais focados em ataques físicos ou habilidades de resistência. Pokémon desses tipos podem compensar sua baixa capacidade de ataque especial com uma abordagem mais direta e física durante as batalhas.')
pdf.paragrafo('Essa distribuição evidencia como o balanceamento do jogo permite que tipos com alta Sp.Atk sejam usados para estratégias baseadas em ataques à distância e controle de campo, enquanto tipos com baixa Sp.Atk geralmente se concentram em resistência e combate direto.')
pdf.image('graficos/4-4-Grafico_spatk_tipo.png', 10, 150, 200)

# Pág 11
pdf.add_page()

pdf.sub_subtitulo_base('2.4.5 Tipos com maior Special Defense')
pdf.paragrafo('O gráfico de barras apresenta a média de Sp.Def(Special Defense) dos Pokémon por tipo. Observa-se que os tipos Fada, Psíquico e Dragão possuem as maiores médias, indicando maior resistência contra ataques especiais e maior probabilidade de funcionarem como "Paredes" ou suporte em batalhas que envolvem dano especial.')
pdf.paragrafo('Em constraste, Ground, Bug e Normal apresentam as menores médias de Sp.Def, sugerindo que esses tipos tendem a privilegiar outros atributos(como atk físico ou velocidade)em vez de defesa especial.')
pdf.paragrafo('Essa distribuição evidencia uma escolha de design em que alguns tipos são orientados para mitigar dano especial e sustentar a equipe, enquanto outros são projetados para papéis mais ofensivos ou especializados.')
pdf.image('graficos/4-5-Grafico_spdef_tipo.png', 10, 150, 200)

# Pág 12
pdf.add_page()

pdf.sub_subtitulo_base('2.4.6 Tipos com maior Speed')
pdf.paragrafo('O gráfico de barras apresenta a média de Speed(Velocidade) dos Pokémon por tipo. Observa-se que os tipos Elétrico, Voador e Dragão possuem os maiores valores médios, indicando maior agilidade e capacidade de atacar antes do oponente, reforçando seu papel em batalhas rápidas e dinâmicas.')
pdf.paragrafo('Em contraste, os tipos Grama, Pedra e Aço apresentam os menores valores médios de Speed, sugerindo um foco em resistência ou poder defensivo em vez de mobilidade.')
pdf.paragrafo('Essa distribuição evidencia uma estratégia de balanceamento do jogo, na qual alguns tipos são projetados para garantir a iniciativa nos combates, enquanto outros são construídos para absorver dano e criar estratégias de longo prazo.')
pdf.image('graficos/4-6-Grafico_speed_tipo.png', 10, 150, 200)

# Pág 13
pdf.add_page()

pdf.sub_subtitulo_base('2.4.7 Tipos com maior Total de stats')
pdf.paragrafo('O gráfico de barras apresenta a média do Total de stats dos Pokémon por tipo. Observa-se que os tipos Dragão, Aço e Psíquico possuem as maiores médias, indicando que esses Pokémon tendem a ser mais completos e versáteis em combate, frequentemente desempenhando papéis centrais nas equipes.')
pdf.paragrafo('Em contraste, os tipos Normal, Inseto e Grama apresentam os menores valores médios, sugerindo que seus representantes ocupam papéis mais básicos ou especializados, sem a mesma abrangência de atributos.')
pdf.paragrafo('Essa distribuição evidencia uma estratégia de balanceamento na franquia, em que certos tipos funcionam como símbolos de poder e raridade, enquanto outros representam acessibilidade e diversidade no início da jornada.')
pdf.image('graficos/4-7-Grafico_total_tipo.png', 10, 150, 200)

# Pág 14
pdf.add_page()

pdf.subtitulo_base('2.5 Análise Comparativa das Gerações com Base nos Stats Totais')
pdf.paragrafo('O gráfico apresenta a média total de stats por geração de Pokémon. A análise revela que a 8ª geração lidera com a maior média(457,6), seguida pela 7ª e 4ª gerações, indicando um aumento gradual na força média dos Pokémon ao longo do tempo.')
pdf.paragrafo('Por outro lado, as gerações 2, 1 e 3 possuem as menores médias, o que reflete o design mais simples e menos voltado para balanceamento competitivo das primeiras eras da franquia.')
pdf.paragrafo('Essa diferença mostra como os criadores foram aumentando a complexidade e o poder dos Pokémon com o passar das gerações, acompanhando a evolução do competitivo e a expectativa dos fãs.')
pdf.paragrafo('No entanto, é importante destacar que Pokémon icônicos das gerações iniciais permanecem relevantes por design, carisma e por receberem evoluções ou formas alternativas em jogos posteriores.')
pdf.image('graficos/5-Grafico_gen_mais_forte.png', 10, 150, 200)

# Pág 15
pdf.add_page()

pdf.subtitulo_base('2.6 Identificação do Tipo Predominante em Cada Geração de Pokémon')
pdf.paragrafo('O gráfico apresenta o tipo predominante em cada geração de Pokémon, revelando como o design dos monstrinhos está intimamente ligado ao ambiente e à inspiração cultural de cada região.')
pdf.paragrafo('Nas 3 primeiras gerações, o tipo Água foi dominante, refletindo a forte presença de mares e lagos em Kanto, Johto e, especialmente em Hoenn. Em seguida, observa-se uma mudança: tipos como Inseto(Gen 4) e Fantasma(Gen 6) se destacam em regiões com florestas densas e castelos sombrios, enquanto Grama(Gen 7) surge em Alola, coerente com a ambientação tropical. O tipo Normal(Gens 5 e 9) aparece com força em Unova e Paldea, regiões inspiradas em locais urbanos ou de grande diversidade cultural, representando o "cotidiano" e a versatilidade. Já o tipo Elétrico(Gen 8) traduz aspecto tecnológico e moderno de Galar.')
pdf.paragrafo('Esses padrões mostram que o tipo predominante não é aleatório: ele reflete tanto o ambiente natural quanto a identidade cultural da região em que os jogos foram baseados, tornando cada geração única em termos de temática e ecossistema Pokémon.')
pdf.image('graficos/6-Grafico_tipo_pred_gen.png', 10, 150, 200)

# Pág 16
pdf.add_page()

pdf.titulo_base('3. Conclusão')
pdf.paragrafo('O presente estudo permitiu uma análise detalhada da Pokédex, revelando padrões e tendências que refletem decisões estratégicas e criativas dos desenvolvedores ao longo das gerações de Pokémon. Observou-se que a distribuição de tipos, a presença de tipos secundários, os status base e a força geral dos Pokémon não são aleatórios, mas cuidadosamente planejados para equilibrar diversidade, aprendizado e complexidade no jogo.')
pdf.paragrafo('A análise dos tipos predominantes por geração mostrou como o design dos Pokémon se relaciona diretamente com a ambientação e a inspiração cultural de cada região, reforçando a identidade única de cada geração. O estudo também evidenciou estratégias de balanceamento entre ofensividade, defesa e velocidade, permitindo que diferentes tipos cumpram papéis específicos nas batalhas, garantindo tanto a acessibilidade para iniciantes quanto desafios para jogadores competitivos.')
pdf.paragrafo('Além disso, o comportamento de Pokémon lendários e a evolução dos stats médios ao longo das gerações indicam uma progressão planejada, que acompanha a complexidade crescente do jogo e as expectativas da comunidade.')
pdf.paragrafo('Em suma, este relatório mostra que a Pokédex é muito mais do que um catálogo: ela reflete escolhas de design que equilibram diversão, desafio e imersão, consolidando Pokémon como uma franquia culturalmente rica e estrategicamente profunda.')

pdf.output('relatorio.pdf')