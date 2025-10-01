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
        self.cell(0, 10, label, 0, 1, 'L')
        self.ln()

    def paragrafo(self, text):
        self.set_font('helvetica', 'B', size=11)
        self.multi_cell(0, 7, text)
        self.ln()

    def imagem(self, img, x, y, w):
        self.image(img, x, y, w)

pdf = PDF()

pdf.add_page()

pdf.titulo('Análise de dados')
pdf.sub_titulo('POKÉMON: ANÁLISE ESTATÍSTICA')
pdf.image('pokemon_relat.jpg', 40, 90, 130)
pdf.ln(160)
pdf.linha_centralizada('Autor: Roger Ferreira de Souza')    

# Pág 1
pdf.add_page()

pdf.titulo_base('Introdução')
pdf.paragrafo('A franquia Pokémon transcendeu o status de simples marca de entretenimento para se tornar parte do imaginário cultural global. Com um valor estimado em mais de 100 bilhões de dólares, ela consolidou-se como a franquia mais valiosa do mundo, presente em múltiplas mídias como jogos, animes e mangás.')
pdf.paragrafo('Apesar dessa relevância, um aspecto central da série permanece pouco explorado: a Pokédex. Introduzida desde o primeiro jogo, sua função principal é catalogar informações sobre os Pokémon. Com o tempo, porém, passou a ser utilizada quase exclusivamente por jogadores competitivos ou fãs mais dedicados.')
pdf.paragrafo('Este estudo tem como objetivo analisar a Pokédex sob uma perspectiva quantitativa, investigando insights interessantes como a distribuição de status base e os tipos predominantes de cada geração,com o intuito de revelar tendências sobre design, ambientação e decisões criativas utilizadas nos jogos. Para isso, utilizamos dados disponibilizados no Kaggle, que oferecem uma visão detalhada das características de cada Pokémon.')

# Pág 2
pdf.add_page()

pdf.titulo_base('Análise dos dados')
pdf.paragrafo('O gráfico de pizza mostra uma vantagem significativa na existência de Pokémons do tipo Água(12,54%) e do tipo Normal(11,18%) em relação ao total, uma causa disso pode se dar ao fato dos 2 tipos serem equilibrados em relação a outros, visto que o tipo Água possui poucas fraquezas(apenas Elétrico e Planta) e do tipo Normal ser um tipo neutro que não possui muitas vantagens e desvantagens, além de serem mais numerosos nas rotas iniciais, o que torna este tipo muito amigável para que jogadores iniciantes se acostumem com a mecânica do jogo, enquanto tipos mais raros como *Dragão* tornam-se alvos de desejo aumentando a emoção ao encontrar, capturar e treinar um deles.')
pdf.paragrafo('Por outro lado, tipos como Gelo(2,30%) e Fada(2,73%) são escassos intencionalmente com a mesma finalidade de manter o equilibrio, o caso do tipo Fada em particular se diferencia do tipo Gelo, pois ele foi introduzido tardiamente nos jogos para ser mais um counter do tipo Dragão, que, por conta de seu baixo número de fraquezas e seus altos stats por muito tempo dominou o game, contudo, os 2 tipos se mantiveram escassos para que o tipo Dragão não perdesse seu impacto na aventura.')
pdf.paragrafo('O tipo Voador(1,02%) tem baixa participação não por ser raro, mas por geralmente aparecer como tipagem secundária, o que o faz ocupar uma posição menor neste estudo baseado apenas nos tipos primários.')
pdf.image('graficos/1-Grafico_porcent_tipo_pkm.png', 10, 155, 200, 140)

# Pág 3
pdf.add_page()

pdf.paragrafo('O gráfico de pizza compara a proporção de Pokémons com e sem tipo secundário. Observa-se que 53,79% possuem um tipo secundário, enquanto 46,21% têm apenas o tipo primário.')
pdf.paragrafo('Essa tendência indica que os designers priorizam combinações de tipos para aumentar a diversidade estratégica, tornando batalhas mais complexas e interessantes.')
pdf.paragrafo('Ao mesmo tempo,a presença significativa de Pokémons de tipo único garante uma base simples e equilibrada, útil para jogadores iniciantes formarem suas estratégias sem a necessidade de estudar a fundo o game e garantir sua diversão mesmo com pouco conhecimento.')
pdf.paragrafo('Essa distribuição evidencia o cuidado no design do jogo e na experiência do jogador, equilibrando diversidade, aprendizado e complexidade.')
pdf.image('graficos/2-Grafico_pkm_tipo_sec.png', 10, 105, 200)

# Pág 4
pdf.add_page()

pdf.paragrafo('O gráfico de barras mostra a quantidade de Pokémons lendários de cada geração.')
pdf.paragrafo('Nota-se um crescimento constante da 1ª geração(5) até a 5ª geração(13), sugerindo uma estratégia de aumentar a diversidade e o apelo desses Pokémons ao longo dos anos. A partir da 6ª geração, entretanto, observa-se uma oscilação, com reduções e novos picos, indicando mudanças na filosofia de design e narrativa. A 9ª geração se destaca por apresentar apenas 2 lendários, possivelmente para reforçar a exclusividade desse grupo ou para priorizar novas mecânicas de jogo.')
pdf.paragrafo('Essa análise revela que a distribuição de lendários não segue uma progressão linear, mas sim reflete escolhas criativas e estratégicas de cada fase da franquia.')
pdf.image('graficos/3-Grafico_lend_gen.png', 10, 105, 200)


pdf.output('teste.pdf')