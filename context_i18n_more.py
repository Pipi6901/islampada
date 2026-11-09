# -*- coding: utf-8 -*-
"""
Lampada — строки контекста на pt, it и ko (с 1.0.2).

Устроено как context_i18n.py: источник истины по смыслу — ru и en в
context_data.py, ключ — id отрывка. Отдельный файл, чтобы не перетряхивать
партии es/fr/de ради двух новых языков. Правила те же: до 34 слов, кто
говорит и при каких обстоятельствах, без толкования и без проповеди.

pt — бразильский португальский, имена как в бразильских Библиях (Davi,
Jó, Bate-Seba). it — итальянский, имена как в итальянской традиции
(Davide, Geremia, Giobbe). ko — стиль сноски на ~다, имена и цитаты как в
개역한글 (다윗, 바벨론, “그리 아니하실지라도”). Строки переведены 07.11.2026.
"""

T_MORE = {
"mat-11-28": dict(
 pt="Jesus diz isso na Galileia, a pessoas esgotadas por um monte de regras religiosas. Ele não se dirige aos fortes, mas aos que já não aguentam mais.",
 it="Gesù lo dice in Galilea, a persone sfinite da una massa di regole religiose. Non si rivolge ai forti, ma a chi non ha più forze.",
 ko="예수께서 갈릴리에서, 수많은 종교 규례에 지친 사람들에게 하신 말씀이다. 강한 이들이 아니라 힘이 다한 이들을 향한 말이다."),
"psa-23-1": dict(
 pt="Salmo de Davi. Ele foi pastor antes de ser rei e sabia por experiência própria o que é guiar um rebanho por ravinas e encontrar água para ele.",
 it="Salmo di Davide. Fu pastore prima di diventare re e sapeva per esperienza che cosa significa guidare un gregge tra i burroni e trovargli l’acqua.",
 ko="다윗의 시다. 그는 왕이 되기 전 목자였고, 양 떼를 이끌고 골짜기를 지나 물을 찾아 주는 일이 무엇인지 몸으로 알았다."),
"isa-41-10": dict(
 pt="Profecia para um povo com medo de desaparecer entre impérios maiores. As palavras não se dirigem aos corajosos, mas a quem já entendeu o quanto é pequeno.",
 it="Profezia per un popolo che teme di scomparire tra imperi più grandi. Le parole non sono rivolte ai coraggiosi, ma a chi ha capito quanto è piccolo.",
 ko="더 큰 제국들 사이에서 사라질까 두려워하는 백성에게 준 예언이다. 용감한 이들이 아니라 자신이 얼마나 작은지 깨달은 이들에게 하는 말이다."),
"php-4-6": dict(
 pt="Paulo escreve isso sob custódia, à espera de julgamento. Quem fala de calma é um homem sem nenhuma garantia sobre o dia de amanhã.",
 it="Paolo scrive sotto sorveglianza, in attesa del processo. L’uomo che parla di calma non ha alcuna garanzia sul domani.",
 ko="바울이 감시를 받으며 재판을 기다리던 중에 쓴 글이다. 평안을 말하는 이 사람에게는 내일에 대한 아무 보장도 없다."),
"jer-29-11": dict(
 pt="De uma carta aos exilados na Babilônia. Jeremias acaba de lhes dizer que construam casas e criem filhos: a volta virá, mas não logo, só daqui a setenta anos.",
 it="Da una lettera agli esuli di Babilonia. Geremia ha appena detto loro di costruire case e crescere figli: il ritorno verrà, ma non presto, tra settant’anni.",
 ko="바벨론 포로들에게 보낸 편지의 일부다. 예레미야는 막 그들에게 집을 짓고 자녀를 낳으라고 했다. 귀환은 오지만 곧은 아니다. 칠십 년 뒤다."),
"rom-8-28": dict(
 pt="Paulo escreve a cristãos de Roma que vivem sob suspeita das autoridades. A frase está num capítulo sobre o sofrimento, não sobre a boa sorte.",
 it="Paolo scrive ai cristiani di Roma, che vivono sotto il sospetto delle autorità. La frase si trova in un capitolo sulla sofferenza, non sulla fortuna.",
 ko="바울이 당국의 의심을 받으며 사는 로마의 그리스도인들에게 쓴 글이다. 이 구절은 행운이 아니라 고난을 다루는 장에 있다."),
"psa-46-1": dict(
 pt="Hino do templo para ser cantado pela congregação. As imagens vêm de terremoto e cerco, coisas que os ouvintes tinham visto pessoalmente, e não imaginado.",
 it="Canto del tempio da intonare in assemblea. Le sue immagini vengono dal terremoto e dall’assedio, cose che gli ascoltatori avevano visto con i propri occhi, non immaginato.",
 ko="함께 부르던 성전 노래다. 그 이미지는 지진과 포위에서 왔다. 듣는 이들이 상상한 것이 아니라 직접 본 일이다."),
"jhn-14-27": dict(
 pt="Dito na noite anterior à prisão, à mesa, a discípulos que ainda não sabem o que está acontecendo. Em poucas horas, todos eles vão se dispersar.",
 it="Detto la notte prima dell’arresto, a tavola, a discepoli che non sanno ancora che cosa sta per accadere. Nel giro di poche ore si disperderanno tutti.",
 ko="체포되기 전날 밤, 식탁에서 아직 무슨 일이 벌어지는지 모르는 제자들에게 하신 말씀이다. 몇 시간 뒤 그들은 모두 흩어진다."),
"1pe-5-7": dict(
 pt="Pedro escreve a cristãos espalhados pela Ásia Menor quando começa a perseguição. O conselho vem de um homem que um dia não aguentou e negou conhecer Jesus.",
 it="Pietro scrive ai cristiani dispersi in Asia Minore mentre inizia la persecuzione. Il consiglio viene da un uomo che un tempo crollò e negò di conoscere Gesù.",
 ko="박해가 시작될 무렵, 베드로가 소아시아에 흩어진 그리스도인들에게 쓴 글이다. 한때 무너져 예수를 모른다고 부인했던 사람의 권면이다."),
"pro-3-5": dict(
 pt="De uma coleção de instruções de um pai ao filho. Sabedoria prática, registrada para um jovem que logo terá de tomar decisões sozinho.",
 it="Da una raccolta di istruzioni che un padre dà al figlio. Saggezza pratica, messa per iscritto per un giovane che sta per iniziare a decidere da solo.",
 ko="아버지가 아들에게 주는 훈계 모음의 일부다. 곧 스스로 결정을 내려야 할 젊은이를 위해 기록한 삶의 지혜다."),
"isa-40-31": dict(
 pt="O início do livro da consolação. O profeta fala a exilados cansados de esperar a volta, a pessoas cujas forças se esgotaram.",
 it="L’inizio del libro della consolazione. Il profeta parla a esuli sfiniti dall’attesa del ritorno, a persone rimaste senza forze.",
 ko="위로의 책이 시작되는 대목이다. 선지자는 귀환을 기다리다 지친 포로들, 힘이 다한 사람들에게 말한다."),
"psa-34-18": dict(
 pt="Salmo de Davi. O título o associa à época em que ele se escondia da morte e se fingiu de louco para sobreviver.",
 it="Salmo di Davide. Il titolo lo collega al periodo in cui fuggiva dalla morte e si finse pazzo per sopravvivere.",
 ko="다윗의 시다. 표제는 이 시를 그가 죽음을 피해 숨어 지내며 살아남으려고 미친 체하던 때와 연결한다."),
"mat-5-4": dict(
 pt="Do Sermão do Monte, pregado numa encosta junto ao mar da Galileia. Os primeiros ouvintes eram pessoas sem dinheiro nem posição, que tinham chegado a pé.",
 it="Dal Discorso della montagna, pronunciato su una collina presso il mare di Galilea. I primi ascoltatori erano persone senza denaro né rango, arrivate a piedi.",
 ko="갈릴리 바다 근처 언덕에서 하신 산상수훈의 일부다. 처음 들은 이들은 돈도 지위도 없이 걸어서 온 사람들이었다."),
"rev-21-4": dict(
 pt="João escreve isso no exílio, na ilha de Patmos, para igrejas onde pessoas estão sendo mortas por causa da fé. O assunto é como tudo termina.",
 it="Giovanni lo scrive in esilio a Patmos, per Chiese in cui si viene uccisi a causa della fede. Parla di come finisce ogni cosa.",
 ko="요한이 밧모 섬에 유배된 채, 믿음 때문에 사람들이 죽임당하는 교회들을 위해 기록했다. 모든 것이 어떻게 끝나는지에 관한 말씀이다."),
"lam-3-22": dict(
 pt="Escrito sobre as ruínas de Jerusalém, depois do cerco e da fome. As palavras sobre fidelidade vêm de um homem que acabou de enterrar sua cidade.",
 it="Scritto sulle rovine di Gerusalemme, dopo l’assedio e la fame. Le parole sulla fedeltà vengono da un uomo che ha appena seppellito la sua città.",
 ko="포위와 기근을 겪은 뒤 예루살렘의 폐허 위에서 쓴 글이다. 신실하심을 말하는 이는 방금 자기 도시를 묻은 사람이다."),
"1th-5-16": dict(
 pt="Da carta mais antiga de Paulo, a uma comunidade com apenas alguns meses de vida. Instruções curtas no fim da carta, quase em forma de lista.",
 it="Dalla più antica lettera di Paolo, a una comunità nata da pochi mesi. Brevi istruzioni alla fine della lettera, quasi un elenco.",
 ko="바울의 가장 이른 편지로, 생긴 지 몇 달밖에 안 된 공동체에 보냈다. 편지 끝에 거의 목록처럼 이어지는 짧은 권면이다."),
"psa-118-24": dict(
 pt="Cântico de ação de graças cantado nas festas junto ao templo. Era lido na Páscoa e, segundo os Evangelhos, Jesus o cantou com os discípulos antes da prisão.",
 it="Canto di ringraziamento intonato presso il tempio durante le feste. Si leggeva nella Pasqua ebraica e, secondo i Vangeli, Gesù lo cantò con i discepoli prima dell’arresto.",
 ko="절기에 성전 곁에서 부르던 감사의 노래다. 유월절에 읽었고, 복음서에 따르면 예수께서 체포 전에 제자들과 이 노래를 부르셨다."),
"col-3-13": dict(
 pt="Paulo escreve da prisão a uma cidade que nunca visitou. Ele fala de pessoas que terão de conviver umas com as outras todos os dias.",
 it="Paolo scrive dal carcere a una città che non ha mai visitato. Parla di persone che dovranno vivere fianco a fianco ogni giorno.",
 ko="바울이 옥에서, 가 본 적 없는 도시에 쓴 편지다. 날마다 서로 부대끼며 살아야 할 사람들에 관한 말이다."),
"eph-4-32": dict(
 pt="De uma carta a Éfeso, cidade portuária onde os cristãos eram uma pequena comunidade mista de judeus e gregos, acostumados a viver separados.",
 it="Da una lettera a Efeso, città portuale dove i cristiani erano una piccola comunità mista di ebrei e greci, abituati a stare separati.",
 ko="항구 도시 에베소에 보낸 편지의 일부다. 그곳 그리스도인은 서로 거리를 두던 유대인과 헬라인이 섞인 작은 공동체였다."),
"mat-6-14": dict(
 pt="Do Sermão do Monte, logo depois do Pai-Nosso. Explica a frase sobre as dívidas que os ouvintes acabaram de ouvir.",
 it="Dal Discorso della montagna, subito dopo il Padre nostro. Spiega la frase sui debiti che gli ascoltatori hanno appena sentito.",
 ko="산상수훈 중 주기도문 바로 뒤에 나온다. 청중이 방금 들은 죄 사함 구절을 풀어 주는 말씀이다."),
"mrk-9-24": dict(
 pt="Fala o pai de um menino doente que os discípulos não conseguiram curar. Ele não é teólogo nem está discutindo: parou de fingir que sua fé é firme.",
 it="Lo dice il padre di un ragazzo malato che i discepoli non erano riusciti a guarire. Non è un teologo e non discute: ha smesso di fingere che la sua fede sia salda.",
 ko="제자들이 고치지 못한 병든 아이의 아버지가 한 말이다. 그는 신학자도 아니고 따지지도 않는다. 믿음이 굳은 척하기를 그만두었을 뿐이다."),
"jhn-20-29": dict(
 pt="Dito a Tomé uma semana depois da ressurreição. Ele tinha se recusado a acreditar nos outros e exigido tocar as feridas, e recebeu essa chance.",
 it="Detto a Tommaso una settimana dopo la risurrezione. Si era rifiutato di credere agli altri e aveva preteso di toccare le ferite, e gli fu concesso.",
 ko="부활 일주일 뒤 도마에게 하신 말씀이다. 그는 다른 제자들의 말을 믿지 않고 상처를 만져 보겠다고 했고, 그럴 기회를 얻었다."),
"jos-1-9": dict(
 pt="Dito a Josué quando ele assume o povo após a morte de Moisés. Um homem que passou quarenta anos como o segundo precisa, pela primeira vez, ir à frente.",
 it="Detto a Giosuè mentre prende la guida del popolo dopo la morte di Mosè. Un uomo che per quarant’anni è stato il secondo deve per la prima volta andare avanti.",
 ko="모세가 죽은 뒤 백성을 맡게 된 여호수아에게 하신 말씀이다. 사십 년을 이인자로 지낸 사람이 처음으로 앞장서야 한다."),
"php-4-13": dict(
 pt="Paulo escreve sob custódia, e a linha anterior explica o que ele quer dizer: aprendeu a viver tanto na fartura quanto na necessidade.",
 it="Paolo scrive sotto sorveglianza, e la frase precedente spiega che cosa intende: ha imparato a vivere sia nell’abbondanza sia nella privazione.",
 ko="바울이 감시 아래에서 쓴 글이며, 바로 앞 구절이 그 뜻을 밝힌다. 그는 풍부할 때도 궁핍할 때도 사는 법을 배웠다."),
"deu-31-6": dict(
 pt="O último discurso de Moisés. Ele tem cento e vinte anos, não entrará na terra prometida e diz isso aos que irão sem ele.",
 it="L’ultimo discorso di Mosè. Ha centovent’anni, non entrerà lui stesso nella terra promessa e lo dice a coloro che ci andranno senza di lui.",
 ko="모세의 마지막 연설이다. 그는 백이십 세이고 약속의 땅에 들어가지 못한다. 자기 없이 그 땅에 갈 이들에게 하는 말이다."),
"psa-4-8": dict(
 pt="Salmo noturno de Davi. Nas linhas anteriores, ele se queixa de pessoas que o caluniam, e mesmo assim se deita para dormir.",
 it="Salmo serale di Davide. Nei versi precedenti si lamenta di chi lo calunnia, eppure si corica a dormire.",
 ko="다윗의 저녁 시다. 앞 구절에서 그는 자신을 헐뜯는 사람들을 두고 탄식하지만, 그래도 누워 잠든다."),
"psa-121-3": dict(
 pt="Cântico de peregrinação, cantado por quem ia a Jerusalém e dormia ao relento numa estrada onde viajantes eram assaltados.",
 it="Canto delle salite, intonato dai pellegrini sulla strada per Gerusalemme, che dormivano all’aperto lungo una via dove i viandanti venivano derubati.",
 ko="예루살렘으로 가는 순례자들이 부르던 성전에 올라가는 노래다. 그들은 강도가 나오는 길에서 한데 잠을 잤다."),
"mat-6-34": dict(
 pt="Do Sermão do Monte. Pouco antes, Jesus fala das aves e dos lírios do campo: seus ouvintes eram pessoas sem garantia de comida para o dia seguinte.",
 it="Dal Discorso della montagna. Poco prima Gesù parla degli uccelli e dei gigli del campo: i suoi ascoltatori non avevano assicurato il cibo del domani.",
 ko="산상수훈의 일부다. 바로 앞에서 예수께서 새와 들의 백합을 말씀하신다. 청중은 내일 먹을 것이 보장되지 않은 사람들이었다."),
"psa-119-105": dict(
 pt="Do salmo mais longo do Saltério, um acróstico do alfabeto hebraico. A lâmpada aqui é uma pequena candeia de barro a óleo, que iluminava um passo, não a estrada toda.",
 it="Dal salmo più lungo del Salterio, un acrostico sull’alfabeto ebraico. La lampada è una piccola lucerna a olio di terracotta che illuminava un passo, non tutta la strada.",
 ko="시편에서 가장 긴 시로, 히브리어 자모 순서로 지었다. 여기서 등은 길 전체가 아니라 한 걸음을 비추던 작은 흙 기름등이다."),
"jhn-3-16": dict(
 pt="De uma conversa noturna com Nicodemos, membro do Sinédrio que veio em segredo para não ser visto com Jesus.",
 it="Da un colloquio notturno con Nicodemo, membro del sinedrio, venuto di nascosto per non farsi vedere con Gesù.",
 ko="니고데모와 밤에 나눈 대화의 일부다. 그는 공회원으로, 예수와 함께 있는 모습을 들키지 않으려고 몰래 찾아왔다."),
"2co-12-9": dict(
 pt="Paulo acaba de falar de uma doença ou defeito do qual pediu três vezes para ser libertado, e não foi. Esta é a resposta que recebeu.",
 it="Paolo ha appena descritto una malattia o un difetto da cui ha chiesto tre volte di essere liberato, senza esserlo. Questa è la risposta che ha ricevuto.",
 ko="바울은 바로 앞에서 세 번이나 없애 달라고 구했으나 없어지지 않은 병이나 결함을 이야기했다. 이것이 그가 받은 대답이다."),
"heb-11-1": dict(
 pt="O início de um capítulo que depois enumera pessoas que morreram sem ver o que fora prometido. A definição vem antes dessa lista, não depois.",
 it="L’inizio di un capitolo che poi elenca persone morte senza aver visto ciò che era stato promesso. La definizione viene prima di quell’elenco, non dopo.",
 ko="약속된 것을 보지 못하고 죽은 사람들을 나열하는 장의 첫머리다. 이 정의는 그 목록 뒤가 아니라 앞에 놓여 있다."),
"psa-139-14": dict(
 pt="Salmo de Davi sobre não haver onde se esconder de Deus. A linha sobre como o ser humano é feito está ao lado de linhas sobre estar sempre à vista.",
 it="Salmo di Davide sull’impossibilità di nascondersi da Dio. Il verso su come è fatto l’essere umano sta accanto a quelli sull’essere sempre visto.",
 ko="하나님을 피해 숨을 곳이 없다는 다윗의 시다. 사람이 어떻게 지어졌는지를 말하는 구절이, 늘 그분 눈앞에 있다는 구절들 곁에 있다."),
"isa-43-2": dict(
 pt="Profecia a um povo que passou pela deportação. Água e fogo aqui não são metáforas genéricas: por trás deles estão a travessia do mar e os incêndios da guerra.",
 it="Profezia a un popolo che ha vissuto la deportazione. Acqua e fuoco qui non sono metafore generiche: dietro ci sono il passaggio del mare e gli incendi della guerra.",
 ko="포로로 끌려간 일을 겪은 백성에게 준 예언이다. 물과 불은 일반적인 비유가 아니다. 그 뒤에는 바다를 건넌 일과 전쟁의 불길이 있다."),
"gal-6-9": dict(
 pt="O fim de uma carta dura aos gálatas, em que Paulo discutiu com eles quase o tempo todo. Na despedida, fala de cansaço, não de quem tem razão.",
 it="La fine di una lettera severa ai Galati, con cui Paolo polemizza quasi dall’inizio alla fine. Congedandosi, parla di stanchezza, non di chi ha ragione.",
 ko="거의 내내 논쟁을 벌인 갈라디아 교인들에게 보낸 날카로운 편지의 끝이다. 작별하며 바울은 자기가 옳다는 말이 아니라 지침에 대해 말한다."),
"gen-1-27": dict(
 pt="A primeira página da Bíblia, o relato da criação. Isso é dito de todos os seres humanos ao mesmo tempo, antes de qualquer divisão em povos, classes ou méritos.",
 it="La prima pagina della Bibbia, il racconto della creazione. È detto di ogni essere umano insieme, prima di qualsiasi divisione in popoli, ranghi o meriti.",
 ko="성경의 첫 페이지, 창조 이야기다. 민족과 신분과 공로로 나뉘기 전, 모든 사람에 대해 한꺼번에 하신 말씀이다."),
"gen-28-15": dict(
 pt="Jacó dorme num lugar ermo, fugindo de um irmão que jurou matá-lo. Sonha com uma escada e ouve isso no sonho.",
 it="Giacobbe dorme in un luogo deserto, in fuga da un fratello che ha giurato di ucciderlo. Sogna una scala e in sogno sente queste parole.",
 ko="야곱은 자신을 죽이겠다고 맹세한 형을 피해 도망치다 빈 들에서 잔다. 그는 꿈에 사닥다리를 보고 이 말씀을 듣는다."),
"gen-50-20": dict(
 pt="José diz isso aos irmãos que um dia o venderam como escravo. O pai deles acaba de morrer, e eles temem que agora José se vingue.",
 it="Giuseppe lo dice ai fratelli che un tempo lo vendettero come schiavo. Il loro padre è appena morto e temono che ora si vendichi.",
 ko="요셉이 한때 자신을 종으로 판 형들에게 하는 말이다. 아버지가 막 죽었고, 형들은 이제 그가 복수할까 두려워한다."),
"exo-14-14": dict(
 pt="O povo está encurralado entre o mar e os carros de guerra que o perseguem. É a resposta de Moisés a uma multidão que já grita que a escravidão teria sido melhor.",
 it="Il popolo è intrappolato tra il mare e i carri che lo inseguono. È la risposta di Mosè a una folla che grida già che era meglio restare schiavi.",
 ko="백성은 바다와 뒤쫓는 병거 사이에 갇혀 있다. 차라리 종으로 사는 편이 나았다고 이미 외치는 무리에게 모세가 한 대답이다."),
"exo-33-14": dict(
 pt="Moisés discute com Deus depois do bezerro de ouro e se recusa a continuar guiando o povo sozinho. Esta é a resposta à sua recusa.",
 it="Mosè discute con Dio dopo il vitello d’oro e si rifiuta di guidare ancora il popolo da solo. Questa è la risposta al suo rifiuto.",
 ko="금송아지 사건 뒤 모세는 하나님과 논쟁하며 더는 혼자 백성을 이끌지 않겠다고 한다. 이것이 그 거절에 대한 대답이다."),
"num-6-24": dict(
 pt="A fórmula de bênção com que os sacerdotes despediam o povo. Era pronunciada em voz alta sobre as pessoas e está entre as orações mais antigas de Israel que se conservaram.",
 it="La formula di benedizione con cui i sacerdoti congedavano il popolo. Veniva pronunciata ad alta voce su di loro ed è tra le più antiche preghiere d’Israele giunte fino a noi.",
 ko="제사장들이 백성을 돌려보낼 때 쓰던 축복 문구다. 사람들 위에 소리 내어 선포했으며, 남아 있는 이스라엘의 가장 오래된 기도 가운데 하나다."),
"deu-6-5": dict(
 pt="Palavras recitadas duas vezes ao dia no judaísmo e escritas nos batentes das portas. Moisés as entrega ao povo antes da entrada na nova terra.",
 it="Parole recitate due volte al giorno nell’ebraismo e scritte sugli stipiti delle porte. Mosè le consegna al popolo prima dell’ingresso nella nuova terra.",
 ko="유대교에서 하루 두 번 암송하고 문설주에 기록하는 말씀이다. 모세가 새 땅에 들어가기 전의 백성에게 준다."),
"jos-24-15": dict(
 pt="Josué reúne o povo no fim da vida e o obriga a escolher abertamente. Muitos naquela assembleia ainda guardam deuses antigos em casa.",
 it="Giosuè raduna il popolo alla fine della sua vita e lo costringe a scegliere apertamente. Molti in quell’assemblea tengono ancora in casa antichi dèi.",
 ko="여호수아가 생애 끝에 백성을 모아 공개적으로 선택하게 한다. 그 모임의 많은 이들이 아직 집에 옛 신들을 두고 있다."),
"1sa-16-7": dict(
 pt="O profeta Samuel escolhe um rei entre os filhos de Jessé e está prestes a ungir o mais alto. Davi nem sequer foi chamado.",
 it="Il profeta Samuele sceglie un re tra i figli di Iesse e sta per ungere il più alto. Davide non è stato nemmeno chiamato.",
 ko="선지자 사무엘이 이새의 아들들 가운데서 왕을 고르며 가장 키 큰 아들에게 기름을 부으려 한다. 다윗은 부름조차 받지 못했다."),
"1ki-19-11": dict(
 pt="Elias foge para o deserto depois das ameaças da rainha e pede para morrer. Espera Deus no vento, no terremoto e no fogo, e não o encontra em nenhum deles.",
 it="Elia fugge nel deserto dopo le minacce della regina e chiede di morire. Aspetta Dio nel vento, nel terremoto e nel fuoco, e non lo trova in nessuno di essi.",
 ko="엘리야는 왕비의 위협을 피해 광야로 도망쳐 죽기를 구한다. 그는 바람과 지진과 불 속에서 하나님을 기다리지만, 어디에서도 만나지 못한다."),
"2ch-20-12": dict(
 pt="O rei Josafá ora em voz alta diante de todo o povo enquanto três exércitos avançam sobre a cidade. Ele admite abertamente que não tem um plano.",
 it="Il re Giosafat prega ad alta voce davanti a tutto il popolo mentre tre eserciti convergono sulla città. Ammette apertamente di non avere alcun piano.",
 ko="세 군대가 한꺼번에 성으로 몰려올 때, 여호사밧 왕이 온 백성 앞에서 소리 내어 기도한다. 그는 아무 계획이 없다고 솔직히 인정한다."),
"neh-8-10": dict(
 pt="O povo ouve a lei lida em voz alta pela primeira vez em décadas e chora. Neemias interrompe o choro: é dia de festa, e ele manda comer e repartir.",
 it="Il popolo sente leggere la legge ad alta voce per la prima volta dopo decenni e piange. Neemia ferma il pianto: è giorno di festa, e dice di mangiare e condividere.",
 ko="백성은 수십 년 만에 처음으로 율법 낭독을 듣고 운다. 느헤미야는 울음을 멈추게 한다. 오늘은 절기이니 먹고 나누라고 한다."),
"job-19-25": dict(
 pt="Jó diz isso depois de perder os filhos, os bens e a saúde, no meio de uma discussão com amigos que insistem que a culpa é dele.",
 it="Giobbe lo dice dopo aver perso figli, beni e salute, nel mezzo di una disputa con amici che insistono che la colpa è sua.",
 ko="욥이 자녀와 재산과 건강을 잃은 채, 다 네 탓이라고 우기는 친구들과 논쟁하던 중에 한 말이다."),
"job-42-5": dict(
 pt="O fim do livro. Deus nunca explica a Jó por que tudo aquilo aconteceu, mas fala com ele. Esta é a resposta de Jó a essa conversa.",
 it="La fine del libro. Dio non spiega mai a Giobbe perché sia accaduto tutto questo, ma parla con lui. Questa è la risposta di Giobbe a quel colloquio.",
 ko="책의 끝이다. 하나님은 왜 이 모든 일이 일어났는지 끝내 설명하지 않으시지만, 욥에게 말씀하신다. 이것은 그 대화에 대한 욥의 대답이다."),
"psa-1-1": dict(
 pt="O salmo que abre todo o Saltério. Está em primeiro lugar como uma porta de entrada: depois vêm cânticos de alegria, ira e desespero, e este apresenta a encruzilhada.",
 it="Il salmo che apre l’intero Salterio. Sta in testa come una porta: seguono canti di gioia, rabbia e disperazione, e questo pone il bivio.",
 ko="시편 전체를 여는 시로, 문처럼 맨 앞에 놓였다. 뒤로 기쁨과 분노와 절망의 노래가 이어지고, 이 시는 갈림길을 제시한다."),
"psa-16-11": dict(
 pt="Salmo de Davi escrito em perigo: nas primeiras linhas, ele pede para ser guardado. As palavras sobre alegria vêm no fim dessa mesma oração.",
 it="Salmo di Davide scritto nel pericolo: nei primi versi chiede di essere protetto. Le parole sulla gioia arrivano alla fine della stessa preghiera.",
 ko="위험 속에서 쓴 다윗의 시다. 첫 구절에서 그는 자신을 지켜 달라고 구한다. 기쁨에 관한 말은 같은 기도의 끝에 나온다."),
"psa-19-1": dict(
 pt="Salmo de Davi que põe lado a lado o céu e a lei, como dois caminhos para conhecer a mesma coisa. A primeira metade fala das estrelas, a segunda dos mandamentos.",
 it="Salmo di Davide che accosta il cielo e la legge come due modi di conoscere la stessa cosa. La prima metà parla di stelle, la seconda di comandamenti.",
 ko="하늘과 율법을 같은 것을 아는 두 길로 나란히 놓은 다윗의 시다. 앞부분은 별에 관해, 뒷부분은 계명에 관해 말한다."),
"psa-27-1": dict(
 pt="Salmo de Davi escrito sob ameaça militar. Luz e fortaleza aqui são palavras do cotidiano de uma cidade sitiada, não abstrações.",
 it="Salmo di Davide scritto sotto minaccia militare. Luce e fortezza sono qui parole del lessico di una città assediata, non astrazioni.",
 ko="군사적 위협 속에서 쓴 다윗의 시다. 여기서 빛과 요새는 추상적 이미지가 아니라 포위된 성에서 쓰던 말이다."),
"psa-27-14": dict(
 pt="A última linha de um salmo que começa confiante e, no meio, desaba num pedido para não ser abandonado. A espera é onde tudo termina.",
 it="L’ultimo verso di un salmo che inizia con fiducia e a metà si spezza in una supplica a non essere abbandonato. Approda all’attesa.",
 ko="자신 있게 시작했다가 중간에 버리지 말아 달라는 간청으로 무너지는 시의 마지막 구절이다. 기다림은 그 끝에 이른 자리다."),
"psa-30-5": dict(
 pt="Cântico para a dedicação de uma casa, escrito depois de uma doença grave. Davi fala de uma noite pela qual acabou de passar, e não da noite de outra pessoa.",
 it="Canto per la dedicazione di una casa, scritto dopo una grave malattia. Davide parla di una notte che ha appena attraversato lui, non un altro.",
 ko="중병을 앓은 뒤에 쓴 낙성가다. 다윗은 남의 밤이 아니라 자신이 막 지나온 밤을 말한다."),
"psa-32-7": dict(
 pt="Salmo sobre admitir a culpa. Nas linhas anteriores, Davi descreve como se calou sobre o que tinha feito e como seus ossos se consumiam.",
 it="Salmo sull’ammissione della colpa. Nei versi precedenti Davide racconta di aver taciuto ciò che aveva fatto e di come le sue ossa si consumavano.",
 ko="죄를 고백하는 시다. 앞 구절에서 다윗은 자기가 한 일을 말하지 않고 침묵하자 뼈가 쇠하던 일을 이야기한다."),
"psa-37-4": dict(
 pt="Salmo de Davi escrito na velhice, como ele mesmo diz mais adiante. O tema é por que os desonestos parecem se dar melhor.",
 it="Salmo di Davide scritto in vecchiaia, come dice più avanti. Il tema è perché i disonesti sembrano passarsela meglio.",
 ko="아래에서 스스로 밝히듯 다윗이 늙어서 쓴 시다. 주제는 왜 악한 자들이 더 잘되는 것처럼 보이는가이다."),
"psa-42-5": dict(
 pt="Salmo de um homem afastado do templo, que lembra como ia até lá no meio da multidão. Ele fala consigo mesmo porque não há mais ninguém por perto.",
 it="Il salmo di un uomo lontano dal tempio, che ricorda quando ci andava in mezzo alla folla. Parla a sé stesso perché non c’è nessun altro.",
 ko="성전에서 떨어져, 무리와 함께 그곳에 가던 때를 떠올리는 사람의 시다. 곁에 아무도 없어 자기 자신에게 말한다."),
"psa-51-10": dict(
 pt="O título liga este salmo ao pior episódio da vida de Davi: depois de Bate-Seba e do assassinato do marido dela, quando o profeta veio confrontá-lo.",
 it="Il titolo collega questo salmo all’episodio peggiore della vita di Davide: dopo Betsabea e l’uccisione di suo marito, quando il profeta venne a metterlo davanti alla sua colpa.",
 ko="표제는 이 시를 다윗 생애의 가장 어두운 일과 연결한다. 밧세바와의 일과 그 남편을 죽인 일 뒤에 선지자가 그를 책망하러 왔을 때다."),
"psa-55-22": dict(
 pt="Salmo sobre a traição de um amigo íntimo: mais acima, Davi escreve que quem o afronta não é um inimigo, mas alguém com quem ele ia ao templo.",
 it="Salmo sul tradimento di un amico intimo: poco sopra Davide scrive che a insultarlo non è un nemico, ma uno con cui andava al tempio.",
 ko="가까운 친구의 배신에 관한 시다. 앞에서 다윗은 자신을 비방하는 자가 원수가 아니라 함께 성전에 다니던 사람이라고 쓴다."),
"psa-56-3": dict(
 pt="O título situa este salmo na época em que Davi caiu nas mãos dos filisteus em Gate. Não foi escrito depois do livramento, mas em meio ao medo.",
 it="Il titolo colloca questo salmo quando Davide cadde nelle mani dei Filistei a Gat. Non è scritto dopo la salvezza, ma dentro la paura.",
 ko="표제는 이 시를 다윗이 가드에서 블레셋 사람에게 잡혔던 때로 본다. 구원받은 뒤가 아니라 두려움 한가운데서 쓴 시다."),
"psa-62-1": dict(
 pt="Salmo de Davi escrito sob a pressão de pessoas que, nas palavras dele, abençoam com a boca e amaldiçoam por dentro.",
 it="Salmo di Davide scritto sotto la pressione di persone che, come dice lui, benedicono con la bocca e maledicono dentro di sé.",
 ko="그의 말대로 입으로는 축복하고 속으로는 저주하는 사람들의 압박 속에서 쓴 다윗의 시다."),
"psa-63-1": dict(
 pt="O título situa este salmo no deserto de Judá, para onde Davi tinha fugido. A sede não é figura de linguagem: ele escreveu isso sem água por perto.",
 it="Il titolo colloca questo salmo nel deserto di Giuda, dove Davide era fuggito. La sete non è una figura retorica: lo scrisse senz’acqua intorno.",
 ko="표제는 이 시를 다윗이 피신한 유다 광야에 둔다. 목마름은 비유가 아니다. 그는 주위에 물이 없는 곳에서 이 시를 썼다."),
"psa-73-26": dict(
 pt="Salmo de um homem que admite ter quase perdido a fé, com inveja do conforto de quem vive desonestamente. É aqui que termina o seu raciocínio.",
 it="Il salmo di un uomo che ammette di aver quasi perso la fede invidiando l’agiatezza di chi vive in modo disonesto. Qui si conclude il suo ragionamento.",
 ko="악하게 사는 이들의 평안을 부러워하다 믿음을 잃을 뻔했다고 고백하는 사람의 시다. 그의 생각은 이 구절에서 결론에 이른다."),
"psa-84-11": dict(
 pt="Cântico de um peregrino com saudade do templo. Ele diz que preferiria estar à porta a habitar nas tendas dos ímpios: compara portas, não ideias.",
 it="Canto di un pellegrino che desidera il tempio. Dice che preferirebbe stare sulla sua soglia che abitare nelle tende dei malvagi: confronta porte, non idee.",
 ko="성전을 그리워하는 순례자의 노래다. 악인의 장막에 사느니 성전 문지기로 있겠다고 한다. 생각이 아니라 문간을 견주는 말이다."),
"psa-90-12": dict(
 pt="O único salmo com o nome de Moisés no título. Fala da brevidade da vida humana, e o pedido aqui é aprender a contar os dias.",
 it="L’unico salmo che porta nel titolo il nome di Mosè. Parla di quanto è breve la vita umana, e qui la richiesta è di imparare a contare i giorni.",
 ko="모세의 이름이 붙은 유일한 시다. 사람의 생애가 얼마나 짧은지를 말하며, 날 계수하는 법을 배우게 해 달라고 구한다."),
"psa-91-1": dict(
 pt="Salmo sobre proteção que enumera perigos bem concretos da época: o terror noturno, a seta de dia e a peste.",
 it="Salmo sulla protezione, che elenca pericoli molto concreti del suo tempo: il terrore notturno, la freccia di giorno e la peste.",
 ko="보호에 관한 시로, 그 시대의 아주 구체적인 위험을 나열한다. 밤의 공포, 낮에 날아드는 화살, 그리고 염병이다."),
"psa-91-11": dict(
 pt="Salmo sobre viver no abrigo do Altíssimo. A promessa sobre os anjos é feita a respeito de um caminho comum: não bater o pé numa pedra.",
 it="Salmo sul vivere al riparo dell’Altissimo. La promessa degli angeli riguarda una strada qualunque: non urtare il piede contro una pietra.",
 ko="지존자의 은밀한 곳에 거하는 삶에 관한 시다. 천사에 관한 약속은 평범한 길, 발이 돌에 부딪히지 않는 일을 두고 한 말이다."),
"psa-94-19": dict(
 pt="Salmo de queixa contra quem oprime viúvas e órfãos e tem certeza de que vai sair impune. A linha sobre consolo está no meio da queixa.",
 it="Salmo che si lamenta di chi opprime vedove e orfani, certo di farla franca. Il verso sulla consolazione sta dentro il lamento.",
 ko="과부와 고아를 짓밟고도 무사하리라 믿는 자들을 탄식하는 시다. 위안에 관한 구절은 그 탄식 한가운데 있다."),
"psa-100-4": dict(
 pt="Salmo curto para a entrada no templo, cantado ao atravessar literalmente as portas rumo aos átrios. Daí as portas no texto.",
 it="Breve salmo per l’ingresso nel tempio, cantato mentre si varcavano davvero le porte verso il cortile. Da qui le porte nel testo.",
 ko="성전에 들어갈 때 부르던 짧은 시로, 실제로 문을 지나 뜰로 들어가며 불렀다. 그래서 본문에 문이 나온다."),
"psa-103-2": dict(
 pt="Salmo de Davi que começa com ele falando consigo mesmo: ordena à própria alma que não se esqueça. Tudo o que se enumera depois é a resposta a essa ordem.",
 it="Salmo di Davide che si apre rivolgendosi a sé stesso: ordina alla propria anima di non dimenticare. Tutto ciò che segue risponde a quell’ordine.",
 ko="자기 자신에게 말을 거는 것으로 시작하는 다윗의 시다. 그는 자기 영혼에게 잊지 말라고 명한다. 뒤에 나열된 모든 것이 그 명령에 대한 답이다."),
"psa-107-1": dict(
 pt="Salmo para os que voltaram do exílio. É feito como uma chamada dos resgatados: cada grupo conta a sua história, e em todas se repete a linha do clamor a Deus.",
 it="Salmo per chi era tornato dall’esilio. È costruito come un appello dei salvati: ogni gruppo racconta la propria storia, con un verso che ritorna.",
 ko="포로에서 돌아온 이들을 위한 시다. 구원받은 이들의 점호처럼 짜여 있어, 무리마다 제 이야기를 하고 한 구절이 되풀이된다."),
"psa-116-1": dict(
 pt="Salmo de um homem que esteve à beira da morte e sobreviveu. Ele diz que invocará Deus a vida inteira porque, uma vez, Deus o ouviu.",
 it="Il salmo di un uomo che era sul punto di morire ed è sopravvissuto. Dice che invocherà Dio per tutta la vita perché una volta lo ha ascoltato.",
 ko="죽을 고비에서 살아난 사람의 시다. 하나님이 한 번 들어 주셨기에 평생 그분을 부르겠다고 한다."),
"psa-126-5": dict(
 pt="Cântico de peregrinação sobre a volta do exílio. A imagem vem da lavoura: o último grão era semeado num ano de fome, sem certeza de colheita.",
 it="Canto delle salite sul ritorno dall’esilio. L’immagine viene dai campi: l’ultimo grano si seminava in un anno di fame, senza certezza del raccolto.",
 ko="포로에서 돌아오는 일을 노래한 성전에 올라가는 노래다. 이미지는 농사에서 왔다. 굶주린 해에 수확을 알 수 없는 채 마지막 씨앗을 뿌렸다."),
"psa-127-2": dict(
 pt="Cântico de peregrinação com o nome de Salomão no título. Fala da inutilidade de trabalhar até a exaustão, dito pelo homem que construiu o templo e o palácio.",
 it="Canto delle salite che porta il nome di Salomone. Parla dell’inutilità di sfinirsi di lavoro, e lo dice l’uomo che costruì il tempio e il palazzo.",
 ko="솔로몬의 이름이 붙은 성전에 올라가는 노래다. 몸이 상하도록 일하는 것이 헛되다는 내용이며, 성전과 왕궁을 지은 사람의 말이다."),
"psa-130-1": dict(
 pt="Cântico de peregrinação que começa do fundo. Em hebraico, “profundezas” é a água em que alguém se afoga; os peregrinos o cantavam na subida.",
 it="Canto delle salite che comincia dal fondo. In ebraico «abissi» indica l’acqua in cui si annega; i pellegrini lo cantavano salendo.",
 ko="밑바닥에서 시작하는 성전에 올라가는 노래다. 히브리어로 “깊은 곳”은 사람이 빠져 죽는 물을 뜻한다. 순례자들은 오르막길에서 이 노래를 불렀다."),
"psa-133-1": dict(
 pt="Cântico de peregrinação entoado quando parentes de todo o país se reuniam em Jerusalém para uma festa e viviam juntos por vários dias.",
 it="Canto delle salite intonato quando parenti da tutto il paese convergevano su Gerusalemme per una festa e vivevano fianco a fianco per diversi giorni.",
 ko="온 나라의 친척들이 절기를 지키러 예루살렘에 모여 며칠을 함께 지낼 때 부르던 성전에 올라가는 노래다."),
"psa-136-1": dict(
 pt="Salmo cantado em alternância: um sacerdote lia uma linha, e o povo respondia com o refrão. O refrão se repete vinte e seis vezes seguidas.",
 it="Salmo cantato a cori alterni: un sacerdote leggeva un verso, il popolo rispondeva con il ritornello. Il ritornello si ripete ventisei volte di seguito.",
 ko="번갈아 부르던 시다. 제사장이 한 줄을 읽으면 백성이 후렴으로 답했다. 후렴은 스물여섯 번 연달아 되풀이된다."),
"psa-143-8": dict(
 pt="Salmo de Davi escrito quando um inimigo, nas palavras dele, tinha esmagado sua vida contra o chão. Quem pede a manhã fala de dentro de uma noite que ainda não acabou.",
 it="Salmo di Davide scritto quando un nemico, come dice lui, gli aveva calpestato la vita a terra. La richiesta del mattino viene da una notte non ancora finita.",
 ko="그의 말대로 원수가 그의 생명을 땅에 엎었을 때 쓴 다윗의 시다. 아침을 구하는 이 말은 아직 끝나지 않은 밤에서 나온다."),
"psa-145-18": dict(
 pt="O último salmo de Davi no Saltério e um acróstico do alfabeto hebraico. Seu tema é que o acesso está aberto a todos, não a alguns escolhidos.",
 it="L’ultimo salmo di Davide nel Salterio e un acrostico sull’alfabeto ebraico. Il tema è che l’accesso è aperto a tutti, non a pochi eletti.",
 ko="시편에 실린 다윗의 마지막 시로, 히브리어 자모 순서로 지었다. 소수의 택한 자가 아니라 모두에게 길이 열려 있다는 내용이다."),
"psa-147-3": dict(
 pt="Salmo escrito depois da volta do exílio e da reconstrução dos muros de Jerusalém. A linha sobre os corações quebrantados fica ao lado de uma linha sobre as estrelas.",
 it="Salmo scritto dopo il ritorno dall’esilio e la ricostruzione delle mura di Gerusalemme. Il verso sui cuori spezzati sta accanto a uno sulle stelle.",
 ko="포로에서 돌아와 예루살렘 성벽을 다시 쌓은 뒤 쓴 시다. 상심한 자에 관한 구절이 별에 관한 구절 곁에 있다."),
"pro-4-23": dict(
 pt="Das instruções de um pai ao filho. A palavra hebraica para coração não fala de sentimentos, mas do lugar onde a pessoa decide e escolhe.",
 it="Dalle istruzioni di un padre al figlio. La parola ebraica per «cuore» non riguarda i sentimenti, ma il luogo in cui una persona decide e sceglie.",
 ko="아버지가 아들에게 주는 훈계의 일부다. 히브리어에서 “마음”은 감정이 아니라 사람이 결정하고 선택하는 자리를 뜻한다."),
"pro-16-9": dict(
 pt="De uma coleção de ditos da corte. Provérbios são observações condensadas, não promessas: a linha descreve como as coisas costumam acontecer, sem garantir o resultado.",
 it="Da una raccolta di detti di corte. I proverbi sono osservazioni condensate, non promesse: il verso descrive come vanno di solito le cose, non garantisce un esito.",
 ko="왕의 잠언 모음의 일부다. 잠언은 약속이 아니라 압축된 관찰이다. 이 구절은 일이 흔히 어떻게 되는지를 말할 뿐, 결과를 보장하지 않는다."),
"pro-17-22": dict(
 pt="De uma coleção de observações curtas sobre a vida cotidiana. Não há aqui nenhuma afirmação médica: é sabedoria popular registrada numa coletânea.",
 it="Da una raccolta di brevi osservazioni sulla vita quotidiana. Non c’è nessuna affermazione medica: è saggezza popolare messa per iscritto in una raccolta.",
 ko="일상생활에 관한 짧은 관찰 모음의 일부다. 의학적 주장이 아니라 모음집에 기록된 민간의 지혜다."),
"pro-18-10": dict(
 pt="A imagem vem da vida urbana da época: a torre dentro das muralhas era o último refúgio quando a cidade já estava sendo tomada.",
 it="L’immagine viene dalla vita cittadina dell’epoca: una torre dentro le mura era l’ultimo rifugio quando la città era già presa.",
 ko="이미지는 당시 도시 생활에서 왔다. 성안의 망대는 성이 함락될 때 사람들이 마지막으로 물러나던 곳이었다."),
"ecc-3-1": dict(
 pt="De um livro cujo autor experimentou riqueza, trabalho e prazer e chamou tudo isso de vaidade. A lista dos tempos vem logo depois dessa conclusão.",
 it="Da un libro il cui autore ha provato ricchezza, lavoro e piacere e ha chiamato tutto un soffio. L’elenco dei tempi viene subito dopo questa conclusione.",
 ko="부와 노동과 쾌락을 다 겪어 보고 모두 헛되다고 한 저자의 책이다. 때에 관한 목록은 그 결론 바로 뒤에 나온다."),
"ecc-4-9": dict(
 pt="Observação de um livro que acaba de descrever um homem que trabalha sem parar e não tem filho, nem irmão, nem ninguém para quem trabalhar.",
 it="Un’osservazione da un libro che ha appena descritto un uomo che lavora senza sosta, senza figli né fratelli, senza nessuno per cui lavorare.",
 ko="아들도 형제도 없고 누구를 위해 일하는지도 모른 채 쉬지 않고 일하는 사람을 막 묘사한 책에 나오는 관찰이다."),
"isa-6-8": dict(
 pt="Isaías vê isso no ano em que morreu o rei Uzias, no momento em que o país perdeu um governante que tinha reinado por cinquenta e dois anos.",
 it="Isaia ha questa visione nell’anno della morte del re Ozia, quando il paese perde un sovrano che aveva regnato cinquantadue anni.",
 ko="이사야가 웃시야 왕이 죽던 해에 본 환상이다. 나라가 오십이 년을 다스린 왕을 잃은 때였다."),
"isa-26-3": dict(
 pt="Uma linha de um cântico que, segundo o profeta, será cantado depois que tudo acabar. Foi escrito de antemão, antes de o desastre terminar.",
 it="Un verso da un canto che, nel testo del profeta, sarà cantato quando tutto sarà finito. È scritto in anticipo, prima che il disastro finisca.",
 ko="선지자의 글에 따르면 모든 일이 끝난 뒤에 부를 노래의 한 구절이다. 재난이 끝나기 전에 미리 쓴 것이다."),
"isa-30-21": dict(
 pt="Dito a um povo prestes a resolver seus problemas com uma aliança com o Egito, sem consultar ninguém. A voz é prometida atrás, não à frente.",
 it="Detto a un popolo che sta per risolvere i suoi problemi con un’alleanza con l’Egitto senza consultare nessuno. La voce è promessa alle spalle, non davanti.",
 ko="누구에게도 묻지 않고 애굽과 동맹을 맺어 문제를 풀려던 백성에게 한 말이다. 그 음성은 앞이 아니라 뒤에서 들려온다고 약속한다."),
"isa-53-5": dict(
 pt="Do cântico do servo sofredor, escrito séculos antes dos acontecimentos do Evangelho e lido pelos cristãos como profecia da crucificação.",
 it="Dal canto del servo sofferente, scritto secoli prima dei fatti del Vangelo e letto dai cristiani come profezia della crocifissione.",
 ko="고난받는 종의 노래 가운데 한 구절이다. 복음서 사건보다 수백 년 앞서 쓰였고, 그리스도인은 이를 십자가 처형의 예언으로 읽는다."),
"isa-55-8": dict(
 pt="Dito a pessoas cuja volta não acontecia do jeito nem no tempo que esperavam. É uma resposta à perplexidade delas, não uma ideia geral.",
 it="Detto a persone il cui ritorno non avveniva né nel modo né nei tempi che si aspettavano. Risponde al loro smarrimento, non enuncia un’idea generale.",
 ko="기대한 방식으로도, 기대한 때에도 귀환이 이루어지지 않던 사람들에게 한 말이다. 일반적인 생각이 아니라 그들의 당혹감에 대한 답이다."),
"isa-61-1": dict(
 pt="Jesus leu este trecho em voz alta na sinagoga de Nazaré, fechou o rolo e disse que ele se cumpria naquele dia. Assim começou o seu ministério.",
 it="Gesù lesse questo passo ad alta voce nella sinagoga di Nazaret, chiuse il rotolo e disse che quel giorno si era compiuto. Così iniziò il suo ministero.",
 ko="예수께서 나사렛 회당에서 이 대목을 소리 내어 읽으시고 두루마리를 덮은 뒤, 오늘 이루어졌다고 하셨다. 그렇게 그분의 사역이 시작되었다."),
"jer-17-7": dict(
 pt="A imagem faz sentido num país com um único rio: a árvore junto à água sobrevive à seca que mata tudo o que cresce longe dele.",
 it="L’immagine ha senso in un paese con un solo fiume: un albero vicino all’acqua sopravvive alla siccità che uccide tutto ciò che cresce lontano.",
 ko="강이 하나뿐인 나라에서는 쉽게 이해되는 이미지다. 물가의 나무는 물에서 떨어져 자라는 모든 것을 죽이는 가뭄을 견딘다."),
"jer-31-3": dict(
 pt="Dito a um povo que acabara de perder o templo, o rei e a terra. A promessa é feita a quem acreditava ter sido abandonado para sempre.",
 it="Detto a un popolo che aveva appena perso il tempio, il re e la terra. La promessa è fatta a chi si credeva abbandonato per sempre.",
 ko="성전과 왕과 땅을 막 잃은 백성에게 한 말이다. 영원히 버림받았다고 믿던 이들에게 준 약속이다."),
"ezk-36-26": dict(
 pt="Ezequiel profetiza no exílio da Babilônia, entre os deportados. Ele não fala de aperfeiçoamento pessoal, mas do que vai acontecer com um povo inteiro.",
 it="Ezechiele profetizza nell’esilio babilonese, tra i deportati. Non parla di miglioramento personale, ma di ciò che accadrà a un intero popolo.",
 ko="에스겔은 바벨론 포로 가운데서 예언한다. 그는 개인의 개선이 아니라 한 백성 전체에 일어날 일을 말한다."),
"dan-3-17": dict(
 pt="Três jovens respondem ao rei que mandou lançá-los na fornalha. As palavras-chave são “mas, se não”: eles não sabem se Deus os salvará.",
 it="Tre giovani rispondono al re che ha ordinato di gettarli in una fornace. Le parole chiave sono «ma anche se non»: non sanno se Dio li salverà.",
 ko="세 젊은이가 자신들을 풀무에 던지라고 명한 왕에게 대답한다. 핵심은 “그리 아니하실지라도”라는 말이다. 그들은 하나님이 구해 주실지 알지 못한다."),
"jol-2-25": dict(
 pt="Profecia após uma praga de gafanhotos que destruiu as colheitas de vários anos seguidos. A promessa diz respeito a anos já vividos em vão.",
 it="Profezia dopo un’invasione di locuste che distrusse diversi raccolti di fila. La promessa riguarda anni già vissuti invano.",
 ko="몇 해 연속 수확을 망친 메뚜기 떼 이후의 예언이다. 약속은 이미 헛되이 지나간 해들에 관한 것이다."),
"mic-6-8": dict(
 pt="Resposta a uma longa lista de sacrifícios que um homem se oferece para trazer. O profeta responde que não é isso que se exige e cita três coisas no lugar.",
 it="Risposta a un lungo elenco di sacrifici che un uomo si offre di portare. Il profeta risponde che non è questo ciò che è richiesto, e nomina invece tre cose.",
 ko="한 사람이 바치겠다고 내놓은 긴 제물 목록에 대한 대답이다. 선지자는 요구되는 것은 그것이 아니라며 세 가지를 든다."),
"hab-3-17": dict(
 pt="O fim de um livro que começou com a pergunta “até quando?”. O profeta enumera a colheita perdida e o gado morto, e termina com um cântico.",
 it="La fine di un libro iniziato con la domanda «fino a quando?». Il profeta elenca raccolti del tutto perduti e bestiame morto, e chiude con un canto.",
 ko="“어느 때까지”라는 질문으로 시작한 책의 끝이다. 선지자는 완전한 흉작과 가축의 죽음을 나열하고, 노래로 책을 마친다."),
"zep-3-17": dict(
 pt="As linhas finais de um livro feito quase só de advertências. Aqui quem se alegra é Deus, e não o povo, uma formulação rara.",
 it="Le righe finali di un libro fatto quasi solo di avvertimenti. Qui è Dio a gioire, non il popolo: una formula rara.",
 ko="거의 경고로만 이루어진 책의 마지막 대목이다. 여기서 기뻐하시는 이는 사람이 아니라 하나님이다. 드문 표현이다."),
"mat-5-14": dict(
 pt="Do Sermão do Monte. Dito não a uma elite, mas à mesma multidão de pobres que, minutos antes, tinha ouvido sobre os pobres de espírito.",
 it="Dal Discorso della montagna. Detto non a un’élite, ma alla stessa folla di poveri che pochi minuti prima aveva sentito parlare dei poveri in spirito.",
 ko="산상수훈의 일부다. 선택된 소수가 아니라, 몇 분 전 심령이 가난한 자에 관한 말씀을 들은 바로 그 가난한 무리에게 하신 말씀이다."),
"mat-6-9": dict(
 pt="Jesus dá esta oração como modelo, ao se opor às longas orações feitas em público. Ela é curta justamente por isso.",
 it="Gesù dà questa preghiera come modello, in polemica con le lunghe preghiere pubbliche. È breve proprio per questo.",
 ko="예수께서 길게 드러내 놓고 하는 기도를 반대하시며 본보기로 주신 기도다. 그래서 짧다."),
"mat-7-7": dict(
 pt="Do Sermão do Monte. Em seguida vem um exemplo doméstico: um pai que não daria ao filho uma pedra em vez de pão.",
 it="Dal Discorso della montagna. Segue un esempio domestico: un padre che non darà al figlio una pietra al posto del pane.",
 ko="산상수훈의 일부다. 뒤이어 집안의 예가 나온다. 아들에게 떡 대신 돌을 주지 않는 아버지다."),
"mat-18-20": dict(
 pt="Dito numa conversa sobre brigas dentro da comunidade e sobre como resolvê-las. O assunto é a reconciliação, não o tamanho da reunião.",
 it="Detto in un discorso sui litigi dentro una comunità e su come risolverli. Il tema è la riconciliazione, non quanta gente si riunisce.",
 ko="공동체 안의 다툼과 그 해결에 관한 대화 중에 하신 말씀이다. 모임의 크기가 아니라 화해에 관한 말이다."),
"mat-22-37": dict(
 pt="Resposta a um perito na lei que veio pô-lo à prova. Jesus junta em um só dois mandamentos de livros diferentes.",
 it="Risposta a un dottore della legge venuto a metterlo alla prova. Gesù unisce in uno solo due comandamenti presi da libri diversi.",
 ko="예수를 시험하러 온 율법사에게 하신 대답이다. 예수께서 서로 다른 책의 두 계명을 하나로 묶으신다."),
"mat-28-20": dict(
 pt="As últimas palavras do Evangelho de Mateus, ditas num monte da Galileia. Duas linhas antes, o texto diz que alguns discípulos duvidaram.",
 it="Le ultime parole del Vangelo di Matteo, pronunciate su un monte in Galilea. Due righe sopra si dice che alcuni discepoli dubitavano.",
 ko="갈릴리의 한 산에서 하신, 마태복음의 마지막 말씀이다. 두 절 앞에는 제자 가운데 몇은 의심했다고 적혀 있다."),
"mrk-10-27": dict(
 pt="Resposta aos discípulos, atônitos depois da conversa com o jovem rico, que perguntaram quem, então, poderia ser salvo.",
 it="Risposta ai discepoli che, sbalorditi dopo il colloquio con il giovane ricco, chiedono chi mai possa essere salvato.",
 ko="부자 청년과의 대화 뒤 놀라서 그러면 누가 구원을 얻을 수 있느냐고 물은 제자들에게 하신 대답이다."),
"luk-1-37": dict(
 pt="Dito pelo anjo a Maria, numa conversa sobre sua parente idosa Isabel, que espera um filho. É um argumento, não um consolo genérico.",
 it="Detto dall’angelo a Maria parlando della sua anziana parente Elisabetta, che aspetta un figlio. È un argomento, non una consolazione generica.",
 ko="천사가 마리아에게, 나이 든 친척 엘리사벳이 아이를 가졌다고 말하는 중에 한 말이다. 일반적인 위로가 아니라 근거로 든 말이다."),
"luk-6-37": dict(
 pt="Do Sermão da Planície, a versão de Lucas do Sermão do Monte. É mais curto e se dirige diretamente aos ouvintes.",
 it="Dal Discorso della pianura, la versione di Luca del Discorso della montagna. È più breve e si rivolge direttamente agli ascoltatori.",
 ko="누가복음에 실린 산상수훈인 평지 설교의 일부다. 더 짧고, 청중에게 직접 하는 말이다."),
"luk-10-41": dict(
 pt="Dito a Marta, que recebeu visitas e cuida sozinha da refeição enquanto a irmã fica sentada ouvindo. Ela se queixou em voz alta.",
 it="Detto a Marta, che ha accolto gli ospiti e prepara da sola il pasto mentre la sorella siede ad ascoltare. Si è lamentata ad alta voce.",
 ko="손님을 맞아 혼자 음식 준비를 하는 마르다에게 하신 말씀이다. 동생은 앉아서 듣고 있었고, 마르다는 소리 내어 불평했다."),
"luk-12-7": dict(
 pt="O argumento se apoia no preço baixo: pardais eram a comida mais miúda dos mais pobres, cinco aves por duas moedas.",
 it="L’argomento si basa sul poco valore: i passeri erano il cibo più modesto dei più poveri, cinque uccelli per due monete.",
 ko="이 논리는 값싼 것에 기대고 있다. 참새는 가난한 이들의 가장 작은 먹거리였고, 동전 두 개에 다섯 마리였다."),
"luk-15-20": dict(
 pt="Da parábola do filho pródigo. O pai corre ao encontro dele, o que era indigno para um homem mais velho daquela época, e os ouvintes sabiam disso.",
 it="Dalla parabola del figliol prodigo. Il padre gli corre incontro, cosa poco dignitosa per un uomo anziano di quel tempo, e gli ascoltatori lo sapevano.",
 ko="탕자의 비유 가운데 한 장면이다. 아버지가 달려 나가는데, 당시 나이 든 남자에게 이는 체면을 잃는 일이었고 청중도 그것을 알았다."),
"luk-23-34": dict(
 pt="Dito da cruz, sobre as pessoas que naquele momento repartiam suas roupas. É a primeira das sete palavras ditas na crucificação.",
 it="Detto dalla croce, riguardo a chi in quel momento si spartiva le sue vesti. È la prima delle sette parole pronunciate durante la crocifissione.",
 ko="십자가 위에서, 그때 그분의 옷을 나누던 사람들을 두고 하신 말씀이다. 십자가에서 하신 일곱 말씀 가운데 첫째다."),
"jhn-1-5": dict(
 pt="Do prólogo do Evangelho, escrito como um hino. O verbo pode significar “não a compreenderam” e “não a venceram”; os tradutores precisam escolher um.",
 it="Dal prologo del Vangelo, scritto come un inno. Il verbo può significare sia «non l’hanno compresa» sia «non l’hanno vinta»; i traduttori devono sceglierne uno.",
 ko="찬송시처럼 쓰인 복음서 서문의 일부다. 원문 동사는 “깨닫지 못하다”와 “이기지 못하다”를 모두 뜻해, 번역자가 하나를 골라야 한다."),
"jhn-8-12": dict(
 pt="Dito no pátio do templo durante a festa dos Tabernáculos, quando enormes candelabros ficavam acesos ali a semana toda. A imagem estava diante dos olhos dos ouvintes.",
 it="Detto nel cortile del tempio durante la festa delle Capanne, quando vi ardevano enormi lampade per tutta la settimana. L’immagine era sotto gli occhi degli ascoltatori.",
 ko="초막절에 성전 뜰에서 하신 말씀이다. 그 주간 내내 그곳에 큰 등불이 타올랐다. 그 이미지가 청중의 눈앞에 있었다."),
"jhn-10-10": dict(
 pt="Do discurso sobre o pastor e o mercenário, feito depois que um cego curado foi expulso da sinagoga por se recusar a voltar atrás.",
 it="Dal discorso sul pastore e sul mercenario, pronunciato dopo che un cieco guarito era stato cacciato dalla sinagoga per essersi rifiutato di ritrattare.",
 ko="목자와 삯군에 관한 말씀의 일부다. 고침받은 맹인이 말을 바꾸지 않아 회당에서 쫓겨난 뒤에 하신 말씀이다."),
"jhn-11-35": dict(
 pt="O versículo mais curto dos Evangelhos. Jesus chora diante do túmulo de Lázaro, sabendo que em poucos minutos o chamará para fora vivo.",
 it="Il versetto più breve dei Vangeli. Gesù piange alla tomba di Lazzaro sapendo che di lì a pochi minuti lo chiamerà fuori vivo.",
 ko="복음서에서 가장 짧은 구절이다. 예수께서 몇 분 뒤 나사로를 살려 불러내실 것을 아시면서도 그의 무덤 앞에서 우신다."),
"jhn-13-34": dict(
 pt="Dito à mesa, logo depois de lavar os pés dos discípulos, tarefa que numa casa cabia ao escravo mais humilde.",
 it="Detto a tavola, subito dopo aver lavato i piedi ai discepoli, un compito che in una casa spettava allo schiavo più umile.",
 ko="식탁에서, 제자들의 발을 씻기신 직후에 하신 말씀이다. 발 씻기는 집안에서 가장 낮은 종이 하던 일이었다."),
"jhn-15-13": dict(
 pt="Dito na noite anterior à prisão, no caminho, saindo do cenáculo. Em poucas horas, as palavras se tornam a descrição do que acontece com ele.",
 it="Detto la notte prima dell’arresto, lungo la strada dal cenacolo. Nel giro di poche ore queste parole diventano la descrizione di ciò che accade a lui.",
 ko="체포 전날 밤, 다락방에서 나와 가는 길에 하신 말씀이다. 몇 시간 뒤 이 말은 그분에게 일어날 일을 그대로 묘사하게 된다."),
"jhn-16-33": dict(
 pt="A última frase do discurso de despedida, antes da oração e da saída para o jardim onde ele é preso. A aflição é prometida abertamente, sem atenuantes.",
 it="L’ultima frase del discorso d’addio, prima della preghiera e del cammino verso il giardino dove verrà arrestato. La tribolazione è annunciata chiaramente, senza attenuazioni.",
 ko="고별 설교의 마지막 문장으로, 기도와 체포될 동산으로 가는 걸음 바로 앞이다. 환난은 누그러뜨림 없이 분명히 예고된다."),
"act-20-35": dict(
 pt="Paulo se despede dos presbíteros de Éfeso sabendo que não os verá mais. Ele cita um dito de Jesus que não está em nenhum Evangelho.",
 it="Paolo saluta gli anziani di Efeso sapendo che non li rivedrà più. Cita un detto di Gesù che non si trova in nessun Vangelo.",
 ko="바울이 다시는 보지 못할 것을 알고 에베소 장로들과 작별한다. 그는 어느 복음서에도 없는 예수의 말씀을 인용한다."),
"rom-5-8": dict(
 pt="Paulo constrói o argumento por contraste: acaba de observar que dificilmente alguém morreria até mesmo por um justo.",
 it="Paolo costruisce l’argomento al contrario: ha appena osservato che a stento qualcuno morirebbe persino per un uomo buono.",
 ko="바울은 반대쪽에서부터 논증한다. 그는 바로 앞에서 의인을 위해서도 죽으려는 사람은 거의 없다고 말했다."),
"rom-12-2": dict(
 pt="O início da parte prática da carta, depois de onze capítulos de argumentação. A partir daqui, Paulo passa ao que fazer.",
 it="L’inizio della parte pratica della lettera, dopo undici capitoli di argomentazione. Da qui Paolo passa a ciò che si deve fare.",
 ko="열한 장에 걸친 논증 뒤, 편지의 실천 부분이 시작되는 곳이다. 여기서부터 바울은 무엇을 해야 하는지로 넘어간다."),
"rom-12-12": dict(
 pt="De uma lista de instruções curtas, uma atrás da outra, sem conectivos. A tribulação aparece nela como um fato dado, não como uma possibilidade.",
 it="Da un elenco di brevi istruzioni che si susseguono senza congiunzioni. La tribolazione vi compare come un dato di fatto, non come un’eventualità.",
 ko="접속어 없이 이어지는 짧은 권면 목록의 일부다. 이 목록에서 환난은 가능성이 아니라 이미 주어진 것으로 나온다."),
"rom-15-13": dict(
 pt="Uma bênção no fim de uma carta a uma comunidade onde judeus e gentios não chegavam a um acordo sobre comida e festas.",
 it="Una benedizione alla fine di una lettera a una comunità dove ebrei e pagani non riuscivano ad accordarsi su cibo e feste.",
 ko="음식과 절기 문제로 유대인과 이방인이 합의하지 못하던 공동체에 보낸 편지 끝의 축복이다."),
"1co-10-13": dict(
 pt="Dito aos coríntios, que se consideravam espiritualmente avançados. Pouco antes, Paulo lhes lembrou como os autoconfiantes morreram no deserto.",
 it="Detto ai Corinzi, che si consideravano spiritualmente avanzati. Poco prima Paolo ha ricordato loro come i troppo sicuri di sé morirono nel deserto.",
 ko="스스로 영적으로 앞섰다고 여기던 고린도 교인들에게 한 말이다. 바울은 앞에서 자신만만하던 이들이 광야에서 어떻게 죽었는지 일깨웠다."),
"1co-13-4": dict(
 pt="Escrito não para casamentos, mas ao tratar das brigas de uma comunidade dividida em facções, que discutiam de quem era o dom espiritual mais importante.",
 it="Scritto non per i matrimoni, ma per sanare i litigi di una comunità divisa in fazioni, che discutevano su quale dono spirituale contasse di più.",
 ko="결혼식을 위해 쓴 글이 아니다. 누구의 은사가 더 중요한지를 두고 파당으로 갈라진 공동체의 다툼을 다루던 중에 쓴 글이다."),
"2co-1-3": dict(
 pt="O início de uma carta em que Paulo logo escreverá que, na Ásia, chegou a desesperar até da própria vida. Ele descreve o consolo como algo que se transmite.",
 it="L’inizio di una lettera in cui Paolo scriverà presto che in Asia disperò perfino della vita. Descrive la consolazione come qualcosa che si trasmette.",
 ko="바울이 곧 아시아에서 살 소망까지 끊어졌다고 쓰게 될 편지의 첫머리다. 그는 위로를 다른 이에게 전해지는 것으로 묘사한다."),
"2co-4-16": dict(
 pt="Paulo escreve isso depois de enumerar espancamentos, naufrágios e fome. A “leve tribulação” é a avaliação que ele mesmo faz da própria lista.",
 it="Paolo scrive questo dopo aver appena elencato percosse, naufragi e fame. La «leggera tribolazione» è il suo giudizio sul suo stesso elenco.",
 ko="바울은 앞에서 매 맞음과 파선과 굶주림을 나열했다. “경한 환난”은 자기 목록에 대한 그 자신의 평가다."),
"2co-5-17": dict(
 pt="De uma carta a uma comunidade que conheceu Paulo antes da conversão, como perseguidor. A afirmação sobre o novo valia, antes de tudo, para ele mesmo.",
 it="Da una lettera a una comunità che aveva conosciuto Paolo prima della conversione, come persecutore. L’affermazione sulla novità valeva anzitutto per lui.",
 ko="회심 전 박해자였던 바울을 알던 공동체에 보낸 편지다. 새로움에 관한 이 말을 그는 무엇보다 자신에게 적용했다."),
"gal-5-22": dict(
 pt="A lista vem logo depois de um catálogo das brigas e invejas que ocupavam a comunidade. Está no singular: um fruto, não nove.",
 it="L’elenco arriva subito dopo un catalogo delle contese e delle invidie che occupavano la comunità. È al singolare: un frutto, non nove.",
 ko="이 목록은 공동체를 사로잡은 다툼과 시기의 목록 바로 뒤에 나온다. 단수형이다. 아홉 열매가 아니라 한 열매다."),
"eph-2-8": dict(
 pt="De uma carta a uma cidade famosa pelo templo de Ártemis e pelo comércio de amuletos, onde a religião era um serviço pago.",
 it="Da una lettera a una città famosa per il tempio di Artemide e il commercio di amuleti, dove la religione era un servizio a pagamento.",
 ko="아데미 신전과 부적 거래로 유명한 도시에 보낸 편지다. 그곳에서 종교는 돈을 내고 받는 서비스였다."),
"eph-3-20": dict(
 pt="O fim da oração com que Paulo encerra a primeira metade da carta. Em seguida começa a parte prática; este é o ponto de virada.",
 it="La fine della preghiera con cui Paolo chiude la prima metà della lettera. Subito dopo inizia la parte pratica; qui sta la cerniera.",
 ko="바울이 편지 전반부를 마무리하는 기도의 끝이다. 다음부터 실천 부분이 시작되니, 여기가 전환점이다."),
"eph-6-10": dict(
 pt="A imagem da armadura vem do soldado romano, visto todos os dias no porto de Éfeso. Paulo escreveu isso estando sob a guarda de homens assim.",
 it="L’immagine dell’armatura è presa dal soldato romano, una vista quotidiana nel porto di Efeso. Paolo la scrisse mentre era sotto la custodia di uomini così.",
 ko="갑옷 이미지는 항구 도시 에베소에서 날마다 보던 로마 군인에게서 왔다. 바울은 그런 군인들에게 갇혀 있으면서 이 글을 썼다."),
"php-1-6": dict(
 pt="Paulo escreve a uma comunidade que ele mesmo fundou e que lhe enviou dinheiro enquanto estava preso. É uma carta de agradecimento.",
 it="Paolo scrive a una comunità fondata da lui stesso, che gli aveva mandato denaro mentre era in prigione. È una lettera di ringraziamento.",
 ko="바울이 직접 세웠고, 그가 옥에 있을 때 돈을 보내 준 공동체에 쓴 편지다. 감사의 편지다."),
"php-2-3": dict(
 pt="Dito a uma comunidade onde, como mostra o fim da carta, duas mulheres brigaram a ponto de Paulo citá-las pelo nome em público.",
 it="Detto a una comunità in cui, come mostra la fine della lettera, due donne avevano litigato così gravemente che Paolo le nomina in pubblico.",
 ko="편지 끝에서 보듯, 두 여인이 심하게 다투어 바울이 공개적으로 이름을 거론한 공동체에 한 말이다."),
"php-4-8": dict(
 pt="Vem logo depois do conselho de não andar ansioso. Paulo propõe não reprimir os pensamentos, mas substituí-los, e lista por quais.",
 it="Arriva subito dopo il consiglio di non angustiarsi. Paolo suggerisce non di reprimere i pensieri, ma di sostituirli, ed elenca con che cosa.",
 ko="염려하지 말라는 권면 바로 뒤에 나온다. 바울은 생각을 억누르지 말고 바꾸라고 하며, 무엇으로 바꿀지 나열한다."),
"col-3-23": dict(
 pt="Dito numa seção sobre deveres domésticos, e as linhas mais próximas se dirigem aos escravos. Os ouvintes eram pessoas que não escolhiam seu trabalho.",
 it="Detto in una sezione sui doveri domestici, con i versi più vicini rivolti agli schiavi. Gli ascoltatori erano persone che non potevano scegliere il proprio lavoro.",
 ko="집안의 의무를 다루는 대목에 나오며, 가장 가까운 구절은 종들에게 하는 말이다. 듣는 이들은 일을 고를 수 없는 사람들이었다."),
"1th-4-13": dict(
 pt="A comunidade tinha enterrado seus primeiros mortos e estava perdida. Paulo não proíbe o luto: ele distingue a tristeza com esperança da tristeza sem ela.",
 it="La comunità aveva sepolto i suoi primi morti ed era smarrita. Paolo non vieta il dolore: distingue il lutto con speranza da quello senza.",
 ko="공동체가 처음으로 죽은 이들을 묻고 당황했다. 바울은 슬퍼하지 말라고 하지 않는다. 소망 있는 슬픔과 소망 없는 슬픔을 구별한다."),
"2ti-1-7": dict(
 pt="A última carta de Paulo, escrita enquanto aguardava a execução, ao jovem Timóteo, que ficou à frente de uma comunidade e, a julgar pelo texto, tinha medo.",
 it="L’ultima lettera di Paolo, scritta in attesa dell’esecuzione al giovane Timoteo, rimasto a guidare una comunità e, a giudicare dal testo, impaurito.",
 ko="바울이 처형을 기다리며 쓴 마지막 편지다. 받는 이는 공동체를 이끌게 된 젊은 디모데로, 본문으로 보아 두려워하고 있었다."),
"heb-4-16": dict(
 pt="A carta se dirige a pessoas acostumadas a um templo onde só um sacerdote se aproximava do lugar santo, uma vez por ano. Daí a palavra “confiança”.",
 it="La lettera è rivolta a persone abituate a un tempio dove solo un sacerdote si avvicinava al luogo santo, una volta l’anno. Da qui la parola «franchezza».",
 ko="제사장만이 일 년에 한 번 지성소에 나아가던 성전에 익숙한 사람들에게 보낸 편지다. 그래서 “담대히”라는 말이 쓰였다."),
"heb-12-1": dict(
 pt="Uma imagem de estádio: as testemunhas nas arquibancadas são as pessoas listadas no capítulo anterior, que morreram sem ver o que fora prometido.",
 it="Un’immagine da stadio: i testimoni sugli spalti sono le persone elencate nel capitolo precedente, morte senza aver visto ciò che era stato promesso.",
 ko="경기장 이미지다. 관중석의 증인들은 앞 장에 나열된, 약속된 것을 보지 못하고 죽은 사람들이다."),
"heb-13-5": dict(
 pt="Uma citação do último discurso de Moisés, feita numa carta a pessoas cujos bens, como o texto diz antes, tinham sido confiscados por causa da fé.",
 it="Una citazione dall’ultimo discorso di Mosè, ripresa in una lettera a persone a cui, come dice il testo più sopra, i beni erano stati confiscati a causa della fede.",
 ko="모세의 마지막 연설을 인용했다. 앞에서 말하듯 믿음 때문에 재산을 빼앗긴 사람들에게 보낸 편지에 나온다."),
"jas-1-2": dict(
 pt="Uma carta a cristãos espalhados pelo império. Tiago não diz que as provações são agradáveis; diz o que fazer com elas.",
 it="Una lettera a cristiani dispersi nell’impero. Giacomo non dice che le prove siano piacevoli; dice che cosa farne.",
 ko="제국 곳곳에 흩어진 그리스도인들에게 보낸 편지다. 야고보는 시험이 즐겁다고 하지 않는다. 그것을 어떻게 다룰지 말한다."),
"jas-1-5": dict(
 pt="Vem logo depois das palavras sobre as provações: a sabedoria pedida aqui não é a sabedoria em geral, mas a necessária para entender uma situação difícil específica.",
 it="Arriva subito dopo le parole sulle prove: la saggezza necessaria non è generica, ma serve a dare un senso a una precisa situazione difficile.",
 ko="시험에 관한 말 바로 뒤에 나온다. 여기서 필요한 지혜는 일반적인 지혜가 아니라 구체적인 어려움을 헤아리기 위한 지혜다."),
"jas-5-16": dict(
 pt="Dito a uma comunidade onde, a julgar pela carta, era normal bajular os ricos e desprezar os pobres. A confissão é proposta como algo mútuo.",
 it="Detto a una comunità in cui, a giudicare dalla lettera, adulare i ricchi e disprezzare i poveri era normale. La confessione è proposta come reciproca.",
 ko="편지로 보아 부자에게 아첨하고 가난한 자를 업신여기는 것이 예사였던 공동체에 한 말이다. 죄의 고백은 서로 하라고 권한다."),
"1pe-4-10": dict(
 pt="Pedro escreve a cristãos que os vizinhos tratavam como estranhos. O conselho de servir uns aos outros é dado a uma comunidade sem apoio de fora.",
 it="Pietro scrive a cristiani che i vicini trattavano da estranei. Il consiglio di servirsi a vicenda è dato a una comunità senza alcun sostegno esterno.",
 ko="베드로가 이웃들에게 외인 취급을 받던 그리스도인들에게 쓴 글이다. 서로 섬기라는 권면은 바깥에 기댈 곳 없는 공동체에 준 것이다."),
"1jn-1-9": dict(
 pt="Carta a uma comunidade onde alguns afirmavam não ter pecado algum. É uma objeção a eles, não uma regra geral.",
 it="Una lettera a una comunità in cui alcuni sostenevano di non avere alcun peccato. È un’obiezione rivolta a loro, non una regola generale.",
 ko="일부 사람들이 자신에게 죄가 전혀 없다고 주장하던 공동체에 보낸 편지다. 일반 규칙이 아니라 그들에 대한 반박이다."),
"1jn-4-18": dict(
 pt="O medo em questão é o medo do castigo, como diz a própria linha. Não é uma promessa de destemor em geral.",
 it="La paura di cui si parla è quella del castigo, come dice il verso stesso. Non è una promessa di non avere mai paura.",
 ko="여기서 말하는 두려움은, 구절 자체가 밝히듯 형벌에 대한 두려움이다. 두려움이 아예 없으리라는 약속이 아니다."),
"rev-3-20": dict(
 pt="Dito à igreja de Laodiceia, cidade rica com água ruim, trazida por aqueduto e que chegava morna. Daí a imagem.",
 it="Detto alla Chiesa di Laodicea, città ricca con un’acqua scadente che arrivava tiepida attraverso un acquedotto. Da qui l’immagine.",
 ko="라오디게아 교회에 하신 말씀이다. 부유한 도시였지만 물이 나빴고, 수로로 끌어온 물은 미지근해져 도착했다. 그래서 그런 비유가 나온다."),
"gen-2-18": dict(
 pt="A primeira coisa que a Bíblia chama de “não boa” não é o pecado, e sim a solidão. Dito antes de tudo se quebrar, quando todo o resto fora chamado de bom.",
 it="La prima cosa che la Bibbia chiama non buona non è il peccato, ma la solitudine. Detto prima che qualcosa si rompesse, quando tutto il resto era stato chiamato buono.",
 ko="성경에서 처음으로 좋지 않다고 한 것은 죄가 아니라 혼자 있는 것이다. 아무것도 망가지기 전, 다른 모든 것이 좋다고 일컬어진 때에 하신 말씀이다."),
"gen-3-9": dict(
 pt="A primeira pergunta que Deus faz a um ser humano na Bíblia. Adão já se escondeu, e a pergunta soa menos como busca do que como chamado para sair do esconderijo.",
 it="La prima domanda che Dio rivolge a un essere umano nella Bibbia. Adamo si è già nascosto, e la domanda suona meno come una ricerca che come un invito a uscire allo scoperto.",
 ko="성경에서 하나님이 사람에게 처음 하신 질문이다. 아담은 이미 숨었고, 이 질문은 찾는 말이라기보다 숨은 자리에서 나오라는 부름처럼 들린다."),
"gen-12-1": dict(
 pt="Abrão tem setenta e cinco anos e recebe a ordem de deixar a cidade onde viveu a vida inteira, sem que lhe digam para onde. Descobre o destino no caminho.",
 it="Abram ha settantacinque anni e gli viene detto di lasciare la città in cui ha sempre vissuto, senza che gli si dica dove andare. Scopre la meta lungo il cammino.",
 ko="아브람은 일흔다섯 살에 평생 살던 성을 떠나라는 말을 듣는다. 어디로 가는지는 듣지 못하고, 목적지는 가는 길에 알게 된다."),
"gen-15-5": dict(
 pt="Abrão já é velho e não tem filhos, e acabou de dizer isso em voz alta. É levado para fora à noite e convidado a contar as estrelas.",
 it="Abram è già vecchio e senza figli, e lo ha appena detto ad alta voce. Viene condotto fuori di notte e gli si dice di contare le stelle.",
 ko="아브람은 이미 늙고 자식이 없으며, 방금 그 사실을 소리 내어 말했다. 그는 밤에 밖으로 이끌려 나가 별을 세어 보라는 말을 듣는다."),
"gen-16-13": dict(
 pt="São palavras de Agar, uma escrava grávida que fugiu da patroa para o deserto. Ela é a primeira pessoa na Bíblia a dar um nome a Deus.",
 it="Sono le parole di Agar, una schiava incinta fuggita nel deserto dalla sua padrona. È la prima persona nella Bibbia a dare un nome a Dio.",
 ko="여주인에게서 도망쳐 광야로 간 임신한 여종 하갈의 말이다. 그녀는 성경에서 하나님께 이름을 붙인 첫 사람이다."),
"gen-32-26": dict(
 pt="Jacó luta a noite toda junto a um vau, na véspera do encontro com o irmão que enganou vinte anos antes. Sairá daquela noite mancando.",
 it="Giacobbe lotta tutta la notte presso un guado, alla vigilia dell’incontro con il fratello che aveva ingannato vent’anni prima. Da quella notte uscirà zoppicando.",
 ko="야곱이 이십 년 전 속인 형을 만나기 전날 밤, 나루에서 밤새 씨름한다. 그는 그 밤을 다리를 절며 떠나게 된다."),
"gen-39-2": dict(
 pt="Dito sobre José no período em que era escravo em terra estrangeira, vendido pelos próprios irmãos. A palavra “próspero” aparece justamente aqui.",
 it="Detto di Giuseppe nel periodo in cui era schiavo in un paese straniero, venduto dai suoi stessi fratelli. La parola «successo» compare proprio qui.",
 ko="요셉이 친형들에게 팔려 타국에서 종으로 지내던 때에 관한 말이다. “형통”이라는 말이 바로 여기에 나온다."),
"exo-3-14": dict(
 pt="Moisés pergunta o que dizer se o povo quiser saber o nome. A resposta é construída sobre o verbo “ser”, e cada edição a traduz à sua maneira.",
 it="Mosè chiede che cosa dire se gli chiederanno un nome. La risposta è costruita sul verbo «essere», e ogni edizione la rende a modo suo.",
 ko="모세는 사람들이 이름을 물으면 무엇이라 답할지 묻는다. 대답은 “있다”라는 동사로 이루어져 있고, 역본마다 저마다의 방식으로 옮긴다."),
"exo-34-6": dict(
 pt="Dito logo depois do bezerro de ouro, quando Moisés talhou novas tábuas para substituir as que quebrou. Profetas e salmos citam essa fórmula mais tarde.",
 it="Detto subito dopo il vitello d’oro, quando Mosè aveva tagliato nuove tavole per sostituire quelle spezzate. Profeti e salmi citeranno poi questa formula.",
 ko="금송아지 사건 직후, 모세가 깨뜨린 돌판 대신 새 돌판을 깎았을 때 하신 말씀이다. 훗날 선지자들과 시편이 이 문구를 인용한다."),
"lev-19-18": dict(
 pt="Uma linha de um código de regras do dia a dia sobre colheitas, pesos e tribunais. Mais tarde, Jesus a chama de segundo maior mandamento, tirando-a dessa lista.",
 it="Un verso da un codice di norme quotidiane su raccolti, pesi e tribunali. Gesù lo chiamerà poi il secondo comandamento più grande, estraendolo da quell’elenco.",
 ko="수확과 저울과 재판에 관한 생활 규례 가운데 한 줄이다. 훗날 예수께서 이를 그 목록에서 꺼내 둘째로 큰 계명이라 부르신다."),
"num-23-19": dict(
 pt="Fala Balaão, um adivinho contratado para amaldiçoar Israel. Ele tenta três vezes e, nas três, pronuncia uma bênção no lugar da maldição.",
 it="Parole di Balaam, un indovino assoldato per maledire Israele. Ci prova tre volte e per tre volte pronuncia invece una benedizione.",
 ko="이스라엘을 저주하도록 고용된 점술가 발람의 말이다. 그는 세 번 시도하고, 세 번 다 저주 대신 축복을 말한다."),
"deu-8-3": dict(
 pt="Moisés explica para que serviram os quarenta anos no deserto. Jesus citará esta mesma linha ao responder à primeira tentação, também no deserto, também com fome.",
 it="Mosè spiega a che cosa sono serviti i quarant’anni nel deserto. Gesù citerà lo stesso verso rispondendo alla prima tentazione, anche lui nel deserto, anche lui affamato.",
 ko="모세가 광야의 사십 년이 무엇을 위한 것이었는지 설명한다. 예수께서 첫 시험에 답하실 때 이 구절을 인용하신다. 그때도 광야였고, 그분도 굶주리셨다."),
"deu-30-19": dict(
 pt="Moisés põe uma escolha diante do povo em seu último discurso e toma o céu e a terra como testemunhas, uma fórmula jurídica de tratado da época.",
 it="Nel suo ultimo discorso Mosè pone il popolo davanti a una scelta e chiama a testimoni il cielo e la terra, una formula giuridica dei trattati dell’epoca.",
 ko="모세는 마지막 연설에서 백성 앞에 선택을 두고 하늘과 땅을 증인으로 부른다. 이는 당시 조약에 쓰던 법적 문구다."),
"deu-31-8": dict(
 pt="Dito a Josué diante de todo o povo. Moisés passa a liderança em público, para que todos vejam o sucessor, e diz que ele não irá à frente sozinho.",
 it="Detto a Giosuè davanti a tutto il popolo. Mosè passa il comando in pubblico perché tutti vedano il successore, e dice che non sarà lui a camminare per primo.",
 ko="온 백성 앞에서 여호수아에게 한 말이다. 모세는 모두가 후계자를 보도록 공개적으로 지도권을 넘기며, 그가 홀로 앞장서지 않으리라고 말한다."),
"jos-1-8": dict(
 pt="Dito a um novo líder no seu primeiro dia. O verbo traduzido como “meditar” significa, em hebraico, murmurar em voz alta: naquela época não se lia em silêncio.",
 it="Detto a un nuovo capo nel suo primo giorno. Il verbo reso con «meditare» in ebraico significa mormorare ad alta voce: allora i testi non si leggevano in silenzio.",
 ko="새 지도자의 첫날에 하신 말씀이다. “묵상하다”로 옮긴 동사는 히브리어로 소리 내어 중얼거린다는 뜻이다. 당시에는 글을 소리 없이 읽지 않았다."),
"jdg-6-12": dict(
 pt="É assim que Gideão é chamado no momento em que malha trigo num lagar, escondido dos saqueadores. Ele logo objeta que deve ser um engano.",
 it="Così viene chiamato Gedeone mentre batte il grano in un torchio, nascosto ai predoni. Obietta subito che dev’esserci un errore.",
 ko="기드온은 약탈자들을 피해 포도주 틀에서 밀을 타작하던 순간 이렇게 불린다. 그는 곧바로 무언가 잘못되었다고 반박한다."),
"rut-1-16": dict(
 pt="Fala Rute, uma estrangeira que ficou viúva jovem. Ela se recusa a voltar para casa e parte com a sogra para um país onde será uma forasteira.",
 it="Parole di Rut, una straniera rimasta vedova giovane. Rifiuta di tornare a casa e parte con la suocera verso un paese dove sarà un’estranea.",
 ko="젊어서 과부가 된 이방 여인 룻의 말이다. 그녀는 고향으로 돌아가기를 거절하고, 자신이 타향 사람이 될 나라로 시어머니와 함께 떠난다."),
"1sa-3-10": dict(
 pt="Samuel tem uns doze anos e três vezes confundiu a voz com a do velho sacerdote. Foi o próprio sacerdote quem lhe ensinou essa resposta.",
 it="Qui Samuele ha circa dodici anni e per tre volte ha scambiato la voce per quella del vecchio sacerdote. È stato il sacerdote a insegnargli questa risposta.",
 ko="사무엘은 이때 열두 살쯤이었고, 세 번이나 그 음성을 늙은 제사장의 음성으로 착각했다. 이렇게 대답하라고 가르쳐 준 이가 바로 그 제사장이다."),
"1sa-17-47": dict(
 pt="Fala um adolescente sem armadura a um homem armado da cabeça aos pés, diante de dois exércitos que estavam frente a frente havia quarenta dias, sem se mover.",
 it="Detto da un ragazzo senza armatura a un uomo armato di tutto punto, davanti a due eserciti schierati l’uno di fronte all’altro da quaranta giorni senza muoversi.",
 ko="갑옷도 없는 소년이 완전 무장한 사람에게 하는 말이다. 사십 일 동안 마주 선 채 움직이지 못하던 두 군대가 지켜보고 있었다."),
"1sa-30-6": dict(
 pt="A cidade de Davi foi incendiada, as famílias de seus homens foram levadas, e os próprios soldados falam em apedrejá-lo. Não há ajuda de ninguém.",
 it="La città di Davide è bruciata, le famiglie dei suoi uomini sono state portate via e i suoi stessi soldati parlano di lapidarlo. Nessuno lo aiuta.",
 ko="다윗의 성읍은 불탔고 부하들의 가족은 사로잡혀 갔으며, 그의 군사들은 그를 돌로 치자고 말한다. 누구에게서도 도움이 없다."),
"1ki-18-21": dict(
 pt="Elias se dirige ao povo no monte Carmelo, onde todos se reuniram. O texto diz que ninguém lhe respondeu uma só palavra.",
 it="Elia si rivolge al popolo radunato al completo sul monte Carmelo. Il testo dice che non gli risposero neanche una parola.",
 ko="엘리야가 모두가 모인 갈멜 산에서 백성에게 말한다. 본문에 따르면 그들은 한마디도 대답하지 않았다."),
"2ki-6-16": dict(
 pt="A cidade está cercada por um exército, e o servo do profeta se apavora. Eliseu pede que os olhos do rapaz se abram, e ele vê o que não via um minuto antes.",
 it="La città è circondata da un esercito e il servo del profeta è nel panico. Eliseo chiede che gli siano aperti gli occhi, e il servo vede ciò che un attimo prima non vedeva.",
 ko="성은 군대에 포위되었고 선지자의 사환은 공포에 질려 있다. 엘리사가 그의 눈을 열어 달라고 구하자, 그는 조금 전까지 보지 못하던 것을 본다."),
"1ch-16-11": dict(
 pt="Do cântico entoado no dia em que a arca finalmente entrou em Jerusalém, após uma pausa de três meses causada por um acidente fatal no caminho.",
 it="Dal canto intonato il giorno in cui l’arca fu finalmente portata a Gerusalemme, dopo una sosta di tre mesi causata da un incidente mortale lungo la strada.",
 ko="하나님의 궤를 마침내 예루살렘에 들인 날 부른 노래의 일부다. 길에서 사람이 죽는 사고로 석 달 동안 멈춘 뒤였다."),
"2ch-7-14": dict(
 pt="Dito a Salomão, à noite, depois da dedicação do templo. A promessa é condicional e dirigida a um povo específico numa terra específica, não a qualquer leitor.",
 it="Detto a Salomone di notte, dopo la dedicazione del tempio. La promessa è condizionata ed è rivolta a un popolo preciso in una terra precisa, non a qualunque lettore.",
 ko="성전 봉헌 뒤 밤에 솔로몬에게 하신 말씀이다. 이 약속은 조건부이며, 아무 독자가 아니라 특정한 땅의 특정한 백성에게 한 것이다."),
"ezr-3-12": dict(
 pt="Lançam-se os alicerces do segundo templo. Os jovens gritam de alegria, os velhos choram porque se lembram do primeiro, e não dava para distinguir um som do outro.",
 it="Si gettano le fondamenta del secondo tempio. I giovani gridano di gioia, gli anziani piangono perché ricordano il primo, e i due suoni non si potevano distinguere.",
 ko="두 번째 성전의 기초를 놓는다. 젊은이들은 기뻐 외치고, 첫 성전을 기억하는 노인들은 운다. 두 소리를 분간할 수 없었다."),
"neh-6-3": dict(
 pt="Resposta a adversários que quatro vezes convidaram Neemias para negociar, a fim de tirá-lo da obra. Ele dá a mesma resposta nas quatro vezes.",
 it="Risposta agli avversari che per quattro volte invitarono Neemia a trattare per allontanarlo dal cantiere. Lui dà la stessa risposta tutte e quattro le volte.",
 ko="느헤미야를 공사 현장에서 떼어 내려고 네 번이나 회담을 청한 적들에게 한 대답이다. 그는 네 번 모두 똑같이 답한다."),
"est-4-14": dict(
 pt="Mardoqueu escreve isso a Ester, uma rainha que esconde sua origem. Apresentar-se ao rei sem ser chamada significava a morte, e ela sabia disso.",
 it="Mardocheo scrive questo a Ester, una regina che nasconde le proprie origini. Presentarsi al re senza essere chiamati significava la morte, e lei lo sapeva.",
 ko="모르드개가 출신을 숨긴 왕비 에스더에게 보낸 말이다. 부름 없이 왕 앞에 나아가면 죽음이었고, 그녀도 그것을 알았다."),
"job-1-21": dict(
 pt="Jó diz isso no dia em que chegaram quatro notícias seguidas: o gado roubado, os servos assassinados e todos os seus dez filhos mortos sob uma casa que desabou.",
 it="Giobbe lo dice il giorno in cui arrivarono quattro notizie una dopo l’altra: bestiame rubato, servi uccisi e tutti e dieci i figli morti sotto il crollo di una casa.",
 ko="가축을 빼앗기고 종들이 죽고 열 자녀가 무너진 집에 깔려 죽었다는 네 소식이 잇달아 온 날, 욥이 한 말이다."),
"job-23-10": dict(
 pt="Jó acaba de dizer que procura Deus e não o encontra nem à frente nem atrás. A linha sobre ser conhecido vem logo depois de admitir que ele mesmo não vê nada.",
 it="Giobbe ha appena detto che cerca Dio e non lo trova né davanti né dietro. Il verso sull’essere conosciuto segue subito l’ammissione di non vedere nulla.",
 ko="욥은 방금 하나님을 찾아도 앞에서도 뒤에서도 만나지 못한다고 했다. 그분이 아신다는 구절은 자신은 아무것도 보지 못한다는 고백 바로 뒤에 온다."),
"psa-3-5": dict(
 pt="O título situa este salmo quando Davi fugia do próprio filho, que liderara uma revolta. Ele escreve que dormiu enquanto era perseguido.",
 it="Il titolo colloca questo salmo quando Davide fuggiva da suo figlio, che aveva scatenato una rivolta. Scrive di aver dormito mentre gli davano la caccia.",
 ko="표제는 이 시를 다윗이 반역한 친아들을 피해 달아나던 때로 본다. 그는 쫓기는 중에도 잠을 잤다고 쓴다."),
"psa-8-3": dict(
 pt="Salmo de Davi escrito, a julgar pelo texto, à noite, a céu aberto. A pergunta sobre o ser humano é feita diante das estrelas, não num templo.",
 it="Salmo di Davide scritto, a giudicare dal testo, di notte a cielo aperto. La domanda sull’uomo è posta davanti alle stelle, non in un tempio.",
 ko="본문으로 보아 밤에 한데서 쓴 듯한 다윗의 시다. 사람에 관한 질문을 성전이 아니라 별을 배경으로 던진다."),
"psa-13-1": dict(
 pt="O salmo começa com quatro “até quando” seguidos. É uma queixa direta contra o silêncio, não uma reflexão piedosa sobre ele.",
 it="Il salmo si apre con quattro domande «fino a quando?» di seguito. È un lamento diretto contro il silenzio, non una pia riflessione su di esso.",
 ko="시는 “어느 때까지”를 네 번 연달아 물으며 시작한다. 침묵에 대한 경건한 묵상이 아니라 정면으로 하는 항의다."),
"psa-20-7": dict(
 pt="Salmo cantado antes de o exército partir. Carros e cavalos eram então o que os tanques são hoje, e Israel quase não os tinha.",
 it="Salmo cantato prima che l’esercito partisse. Carri e cavalli erano allora ciò che oggi sono i carri armati, e Israele non ne aveva quasi.",
 ko="군대가 출정하기 전에 부르던 시다. 당시 병거와 말은 오늘날의 탱크와 같았고, 이스라엘에는 그것이 거의 없었다."),
"psa-22-1": dict(
 pt="Salmo de Davi que começa com um grito de abandono. Jesus diz esta linha na cruz, e quem ouvia sabia como o salmo termina.",
 it="Salmo di Davide che si apre con un grido di abbandono. Gesù pronuncia questo verso dalla croce, e chi ascoltava sapeva come finisce il salmo.",
 ko="버림받았다는 부르짖음으로 시작하는 다윗의 시다. 예수께서 십자가에서 이 구절을 외치시며, 듣던 이들은 이 시가 어떻게 끝나는지 알고 있었다."),
"psa-25-4": dict(
 pt="Um acróstico do alfabeto hebraico: cada linha começa com a letra seguinte. O pedido pelo caminho e o pedido de perdão aparecem lado a lado.",
 it="Un acrostico sull’alfabeto ebraico: ogni verso comincia con la lettera successiva. La richiesta sulla via e quella di perdono stanno l’una accanto all’altra.",
 ko="각 줄이 히브리어 자모 순서대로 시작하는 시다. 길을 구하는 간구와 용서를 구하는 간구가 나란히 놓여 있다."),
"psa-31-15": dict(
 pt="Salmo de um homem que escreve ter sido esquecido como um morto e ouve cochichos ao seu redor. As palavras sobre o tempo são ditas a partir dessa situação.",
 it="Il salmo di un uomo che scrive di essere dimenticato come un morto e di sentire bisbigli intorno a sé. Le parole sul tempo sono dette da questa condizione.",
 ko="죽은 자처럼 잊혔고 주위에서 수군거림을 듣는다고 쓰는 사람의 시다. 때에 관한 말은 그런 처지에서 나온 것이다."),
"psa-34-8": dict(
 pt="O convite se baseia no paladar, o mais corporal dos sentidos. O salmo foi escrito depois que Davi escapou por pouco fingindo-se de louco.",
 it="L’invito si basa sul gusto, il più corporeo dei sensi. Il salmo fu scritto dopo che Davide era scampato per un pelo fingendosi pazzo.",
 ko="초대는 가장 몸에 가까운 감각인 맛에 기대어 있다. 이 시는 다윗이 미친 체하여 간신히 살아난 뒤에 쓰였다."),
"psa-40-1": dict(
 pt="Salmo de Davi sobre ser tirado de um poço de lama. A expressão traduzida como “com paciência” significa literalmente “esperei e esperei”.",
 it="Salmo di Davide sull’essere tirato fuori da una fossa di fango. La parola resa con «pazientemente» significa letteralmente «ho atteso e atteso».",
 ko="웅덩이와 수렁에서 건져진 일을 노래한 다윗의 시다. “기다리고 기다렸더니”는 원문에서도 같은 말을 거듭한 표현이다."),
"psa-46-10": dict(
 pt="A linha está num salmo em que a terra treme e as lanças se quebram. O verbo hebraico está mais perto de “deixem cair as mãos” do que de “aquietem-se”.",
 it="Il verso sta in un salmo in cui la terra crolla e le lance si spezzano. Il verbo ebraico è più vicino a «lasciate cadere le mani» che a «tacete».",
 ko="땅이 흔들리고 창이 꺾이는 시에 있는 구절이다. “가만히 있어”로 옮긴 히브리어 동사는 “조용히 하라”보다 “손을 내려놓으라”에 가깝다."),
"psa-61-2": dict(
 pt="Davi escreve que clama desde os confins da terra quando o coração desfalece. Não pede força, mas ser erguido mais alto do que conseguiria subir sozinho.",
 it="Davide scrive che grida dai confini della terra quando il suo cuore viene meno. Non chiede forza, ma di essere portato più in alto di quanto riesca a salire.",
 ko="다윗은 마음이 눌릴 때 땅 끝에서 부르짖는다고 쓴다. 힘을 달라는 것이 아니라, 스스로 오를 수 없는 높은 곳으로 이끌어 달라는 간구다."),
"psa-68-6": dict(
 pt="Salmo de procissão, cantado durante o transporte do santuário. A linha sobre órfãos e solitários aparece numa lista daquilo de que Deus cuida primeiro.",
 it="Salmo processionale cantato mentre si portava il santuario. Il verso sugli orfani e su chi è solo compare in un elenco di ciò di cui Dio si occupa per primo.",
 ko="성소를 옮길 때 부르던 행진의 시다. 고아와 고독한 자에 관한 구절은 하나님이 먼저 돌보시는 것들의 목록에 있다."),
"psa-71-9": dict(
 pt="Salmo de um idoso: ele escreve que confia em Deus desde a juventude e pede para não ser abandonado agora, quando as forças acabam. É uma oração sobre a velhice.",
 it="Salmo di un anziano: scrive di aver confidato in Dio fin dalla giovinezza e chiede di non essere abbandonato ora che le forze vengono meno. È una preghiera sulla vecchiaia.",
 ko="노인의 시다. 그는 어려서부터 하나님을 의지했다며, 힘이 다해 가는 지금 버리지 말아 달라고 구한다. 늙음에 관한 기도다."),
"psa-77-11": dict(
 pt="Salmo de um homem que não consegue dormir e pergunta se Deus se esqueceu de ter misericórdia. Ele decide lembrar o passado porque o presente não lhe diz nada.",
 it="Il salmo di un uomo che non riesce a dormire e si chiede se Dio abbia dimenticato di avere pietà. Si volge al passato perché il presente non gli dice nulla.",
 ko="잠 못 이루며 하나님이 은혜 베풀기를 잊으셨는지 묻는 사람의 시다. 현재가 아무것도 말해 주지 않기에 그는 지난 일을 기억하기로 한다."),
"psa-86-11": dict(
 pt="Um pedido por um coração não dividido: literalmente, deixar de querer coisas opostas ao mesmo tempo. O salmo foi escrito em perigo, sob ameaça de homens violentos.",
 it="La richiesta di un cuore indiviso, cioè letteralmente di smettere di volere cose opposte nello stesso momento. Il salmo è scritto sotto la minaccia di uomini violenti.",
 ko="“일심”을 구하는 기도로, 문자 그대로 서로 반대되는 것을 한꺼번에 원하지 않게 해 달라는 뜻이다. 강포한 자들의 위협 속에서 쓴 시다."),
"psa-88-18": dict(
 pt="O único salmo que termina sem alívio: a última palavra é “trevas”. Ele não chega a consolo algum, e isso foi deixado como está.",
 it="L’unico salmo che finisce senza sollievo: l’ultima parola è tenebra. Non arriva ad alcuna consolazione, ed è stato lasciato così com’è.",
 ko="위안 없이 끝나는 유일한 시다. 마지막 말은 흑암이다. 어떤 위로에도 이르지 않으며, 그대로 남겨 두었다."),
"psa-102-17": dict(
 pt="O título chama este salmo de oração de um aflito que derrama sua angústia. O autor diz que está sozinho como um pássaro no telhado.",
 it="Il titolo lo chiama la preghiera di un afflitto che sfoga la sua pena. L’autore dice di stare solo come un uccello sul tetto.",
 ko="표제는 이 시를 근심을 토하는 곤고한 자의 기도라고 부른다. 그는 지붕 위의 외로운 새처럼 홀로 앉아 있다고 쓴다."),
"psa-112-7": dict(
 pt="Um acróstico sobre a pessoa que vive com honestidade. A linha não promete que não haverá más notícias; fala de como elas são recebidas.",
 it="Un acrostico su una persona che vive onestamente. Il verso non promette che non arriveranno cattive notizie; parla di come accoglierle.",
 ko="정직하게 사는 사람에 관한, 자모 순서로 지은 시다. 이 구절은 흉한 소식이 없으리라고 약속하지 않는다. 그것을 어떻게 맞는지를 말한다."),
"psa-113-7": dict(
 pt="Um salmo do ciclo da Páscoa. A imagem é literal: os pobres da época se sentavam no pó junto às portas da cidade e nos montes de lixo fora dela.",
 it="Un salmo del ciclo pasquale. L’immagine è letterale: i poveri di allora sedevano nella polvere presso le porte e sui mucchi di rifiuti fuori città.",
 ko="유월절에 부르던 시들 가운데 하나다. 이미지는 문자 그대로다. 당시 가난한 이들은 성문 곁 먼지와 성 밖 거름더미에 앉아 있었다."),
"psa-118-6": dict(
 pt="O último salmo do Hallel da Páscoa, cantado no fim da ceia pascal. Quem fala é um homem que foi cercado por todos os lados e saiu com vida.",
 it="L’ultimo salmo dell’Hallel pasquale, cantato alla fine della cena di Pasqua. Chi parla è un uomo che era stato accerchiato da ogni parte e ne è uscito vivo.",
 ko="유월절 할렐의 마지막 시로, 유월절 식사 끝에 불렀다. 말하는 이는 사방으로 에워싸였다가 살아 나온 사람이다."),
"psa-119-71": dict(
 pt="Uma linha do acróstico sobre a lei. O autor fala da própria aflição no passado: ele a avalia já do outro lado.",
 it="Un verso dell’acrostico sulla legge. L’autore parla della propria sofferenza al passato: la valuta dall’altra sponda.",
 ko="율법에 관한 자모 순서 시의 한 구절이다. 저자는 자신의 고난을 과거형으로 말한다. 이미 빠져나와서 그것을 돌아보는 것이다."),
"psa-122-1": dict(
 pt="Cântico de peregrinação sobre o momento da chegada. Os peregrinos caminhavam por dias, e a alegria aqui é que seus pés enfim estão parados às portas.",
 it="Canto delle salite sul momento dell’arrivo. I pellegrini camminavano per giorni, e la gioia qui è che i loro piedi stanno finalmente dentro le porte.",
 ko="도착하는 순간을 노래한 성전에 올라가는 노래다. 순례자들은 여러 날을 걸었고, 여기서 기쁨은 마침내 발이 성문 안에 섰다는 데 있다."),
"psa-125-2": dict(
 pt="Cântico de peregrinação. A imagem é literal: Jerusalém fica cercada de montes, e os peregrinos os viam durante toda a subida.",
 it="Canto delle salite. L’immagine è letterale: Gerusalemme sta in un cerchio di colline, e i pellegrini le vedevano per tutta la salita.",
 ko="성전에 올라가는 노래다. 이미지는 문자 그대로다. 예루살렘은 산들로 둘러싸여 있고, 순례자들은 올라가는 내내 그 산들을 보았다."),
"psa-131-2": dict(
 pt="O mais curto dos salmos de Davi. A imagem é precisa: uma criança desmamada já não exige leite e simplesmente fica deitada junto à mãe.",
 it="Il più breve dei salmi di Davide. L’immagine è precisa: un bambino svezzato non pretende più il latte e semplicemente riposa accanto alla madre.",
 ko="다윗의 시 가운데 가장 짧은 시다. 이미지가 정확하다. 젖 뗀 아이는 더 이상 젖을 조르지 않고 어머니 곁에 그저 누워 있다."),
"psa-134-1": dict(
 pt="O último cântico de peregrinação, dirigido aos que faziam o plantão noturno no templo. Os peregrinos que partiam o cantavam para os vigias que ficavam.",
 it="L’ultimo canto delle salite, rivolto a chi era di turno di notte nel tempio. I pellegrini in partenza lo cantavano alle sentinelle che restavano.",
 ko="마지막 성전에 올라가는 노래로, 밤에 성전에서 섬기는 이들을 향한다. 떠나는 순례자들이 남아 있는 파수꾼들에게 불렀다."),
"psa-137-1": dict(
 pt="Escrito no exílio da Babilônia. Pediam aos cativos que cantassem uma de suas canções para diverti-los; o salmo fala da recusa.",
 it="Scritto nell’esilio babilonese. Ai prigionieri fu chiesto di cantare uno dei loro canti per divertire; il salmo parla del rifiuto.",
 ko="바벨론 포로 중에 쓴 시다. 포로들은 흥을 돋우려 자기들 노래를 불러 보라는 요구를 받았다. 이 시는 그것을 거절하는 내용이다."),
"psa-139-7": dict(
 pt="Davi percorre os lugares onde alguém poderia se esconder: o céu, a sepultura, o outro lado do mar. A lista é feita como uma tentativa, não como consolo.",
 it="Davide passa in rassegna i luoghi in cui ci si potrebbe nascondere: i cieli, la tomba, l’estremità del mare. L’elenco è un tentativo, non una consolazione.",
 ko="다윗은 숨을 만한 곳을 하나씩 짚는다. 하늘, 음부, 바다 끝이다. 이 목록은 위로가 아니라 시도로 쓰였다."),
"psa-141-3": dict(
 pt="Oração de Davi ao entardecer. Ele pede que se ponha uma guarda na própria boca, ou seja, sobre aquilo que ele mesmo não consegue governar.",
 it="Preghiera serale di Davide. Chiede che si metta una guardia alla sua stessa bocca, cioè a ciò che non riesce a governare da solo.",
 ko="다윗의 저녁 기도다. 자기 입에 파수꾼을 세워 달라고, 곧 스스로 다스리지 못하는 것을 지켜 달라고 구한다."),
"psa-142-4": dict(
 pt="O título situa este salmo quando Davi se escondia numa caverna. Ele escreve que olha para a direita e não vê ninguém que o conheça.",
 it="Il titolo colloca questo salmo quando Davide si nascondeva in una caverna. Scrive di guardare alla sua destra e di non vedere nessuno che lo conosca.",
 ko="표제는 이 시를 다윗이 굴에 숨어 있던 때로 본다. 그는 오른쪽을 보아도 자기를 아는 이가 아무도 없다고 쓴다."),
"psa-146-5": dict(
 pt="O salmo adverte contra confiar em príncipes, porque o fôlego deles se vai e seus planos morrem no mesmo dia. O conselho é prático, não poético.",
 it="Il salmo mette in guardia dal confidare nei principi, perché il loro respiro se ne va e i loro progetti muoiono lo stesso giorno. Il consiglio è pratico, non poetico.",
 ko="이 시는 방백들을 의지하지 말라고 경고한다. 그들의 호흡이 끊어지면 그날로 계획도 사라지기 때문이다. 시적인 말이 아니라 실제적인 조언이다."),
"pro-11-25": dict(
 pt="De uma coleção de ditos curtos. A imagem vem da lavoura: a generosidade é descrita como regar, e quem rega também se molha.",
 it="Da una raccolta di brevi detti. L’immagine è agricola: la generosità è descritta come un’irrigazione in cui anche chi annaffia si bagna.",
 ko="짧은 격언 모음의 일부다. 이미지는 농사에서 왔다. 너그러움을 물 주기에 빗대는데, 물을 주는 사람도 함께 젖는다."),
"pro-12-25": dict(
 pt="Uma observação de que a ansiedade pesa fisicamente sobre a pessoa. O remédio indicado é simples e está ao alcance de qualquer um: uma boa palavra.",
 it="Un’osservazione: l’ansia schiaccia fisicamente una persona. Il rimedio indicato è semplice e alla portata di tutti: una buona parola.",
 ko="근심이 사람을 몸으로도 짓누른다는 관찰이다. 처방은 단순하고 누구나 할 수 있는 것, 선한 말 한마디다."),
"pro-15-1": dict(
 pt="Um dito de uma coleção da corte: essas regras eram reunidas para quem teria de falar com reis e conduzir negociações.",
 it="Un detto da una raccolta di corte: regole del genere venivano raccolte per chi avrebbe dovuto parlare con i re e condurre trattative.",
 ko="궁중 격언 모음에 있는 말이다. 이런 규칙은 왕과 말하고 협상을 해야 할 사람들을 위해 모은 것이다."),
"pro-24-16": dict(
 pt="Na contagem hebraica, sete não é um número exato, mas “quantas vezes for”. A linha não descreve alguém que nunca falha, mas a capacidade de se levantar.",
 it="Nel modo di contare ebraico, sette non è un numero esatto ma «un numero indefinito di volte». Il verso non descrive l’essere senza errori, ma la capacità di rialzarsi.",
 ko="히브리식 셈에서 일곱은 정확한 수가 아니라 “몇 번이든”이라는 뜻이다. 이 구절은 실수하지 않는 것이 아니라 다시 일어나는 힘을 말한다."),
"pro-27-17": dict(
 pt="Imagem da forja: o ferro é afiado pelo ferro, e o processo é barulhento e solta faíscas. O dito não é sobre concordância, mas sobre atrito.",
 it="Un’immagine di fucina: il ferro si affila con il ferro, e il procedimento è rumoroso e fa scintille. Il detto non parla di accordo, ma di attrito.",
 ko="대장간 이미지다. 철은 철로 다듬으며, 그 과정은 시끄럽고 불꽃이 튄다. 이 격언은 의견 일치가 아니라 마찰에 관한 것이다."),
"pro-29-25": dict(
 pt="O “laço” aqui é a armadilha de um caçador de pássaros. O dito fala do medo das pessoas, não do medo do perigo.",
 it="Il «laccio» qui è una trappola da cacciatore per uccelli. Il detto parla della paura della gente, non della paura del pericolo.",
 ko="여기서 “올무”는 새를 잡는 사냥꾼의 덫이다. 이 격언은 위험에 대한 두려움이 아니라 사람에 대한 두려움에 관한 것이다."),
"ecc-9-11": dict(
 pt="O autor enumera: nem sempre os velozes vencem a corrida, nem sempre os sábios têm o que comer. É uma observação que vai contra o restante de Provérbios.",
 it="L’autore lo elenca: non sempre i veloci vincono la corsa, non sempre i saggi hanno pane. È un’osservazione che va contro il resto dei Proverbi.",
 ko="저자는 하나하나 든다. 빠른 자가 늘 경주에서 이기지 않고, 지혜로운 자가 늘 배부르지 않다. 잠언의 나머지 내용과 어긋나는 관찰이다."),
"ecc-12-13": dict(
 pt="Últimas linhas de um livro que chamou tudo de vapor. A conclusão é breve e deliberadamente modesta, depois de doze capítulos testando opções.",
 it="Le ultime righe di un libro che ha definito tutto vanità. La conclusione è breve e volutamente modesta, dopo dodici capitoli passati a vagliare alternative.",
 ko="모든 것을 헛되다고 한 책의 마지막 구절이다. 열두 장에 걸쳐 여러 길을 시험해 본 뒤에 내린 결론은 짧고 일부러 소박하다."),
"sng-8-6": dict(
 pt="De um livro que nunca menciona Deus e é feito inteiramente das falas de dois amantes. Um selo sobre o coração é imagem de posse, não de enfeite.",
 it="Da un libro che non nomina mai Dio ed è fatto interamente delle parole di due innamorati. Il sigillo sul cuore è un’immagine di possesso, non di ornamento.",
 ko="하나님이 한 번도 언급되지 않고 두 연인의 말로만 이루어진 책에서 나온다. 마음에 품는 인(도장)은 장식이 아니라 소유를 나타내는 이미지다."),
"isa-1-18": dict(
 pt="Dito na abertura do livro, logo após a acusação de que se ofereciam sacrifícios enquanto os pobres eram esmagados. O corante carmesim daquela época não saía com a lavagem.",
 it="Detto all’inizio del libro, subito dopo l’accusa di offrire sacrifici mentre si opprimono i poveri. La tintura scarlatta di quel tempo non si lavava via.",
 ko="책의 첫머리, 제사는 드리면서 가난한 자는 짓밟는다는 고발 바로 뒤에 나온다. 당시의 주홍 염료는 빨아도 지워지지 않았다."),
"isa-9-2": dict(
 pt="Dito sobre os distritos do norte que a Assíria devastou primeiro. Mais tarde, o Evangelho de Mateus aplica esta frase ao início do ministério na Galileia.",
 it="Detto dei distretti del nord, i primi devastati dall’Assiria. Il Vangelo di Matteo applicherà poi questa frase all’inizio del ministero in Galilea.",
 ko="앗수르가 가장 먼저 짓밟은 북쪽 지역을 두고 한 말이다. 훗날 마태복음은 이 구절을 갈릴리에서 시작된 사역에 적용한다."),
"isa-35-3": dict(
 pt="Dirigido não aos fortes, mas a quem deve sustentar os outros: fortalecer as mãos alheias, falar ao coração alheio. A tarefa é entregue a pessoas.",
 it="Rivolto non ai forti, ma a chi deve sostenere gli altri: rafforzate le mani altrui, parlate al cuore altrui. Il compito è affidato alle persone.",
 ko="강한 자가 아니라 남을 붙들어 주어야 할 사람들에게 하는 말이다. 남의 손을 강하게 하고 남의 마음에 말하라는 것으로, 그 일이 사람에게 맡겨진다."),
"isa-40-11": dict(
 pt="Vem logo depois de linhas sobre o poder que segura as águas e os montes. A escala muda de repente: o mesmo leva cordeiros junto ao peito.",
 it="Viene subito dopo le righe sulla potenza che regge le acque e i monti. L’immagine cambia scala di colpo: lo stesso porta gli agnelli stretti al petto.",
 ko="물과 산을 붙드는 능력을 말한 구절 바로 뒤에 나온다. 그림의 크기가 갑자기 바뀐다. 같은 이가 어린 양을 품에 안는다."),
"isa-42-3": dict(
 pt="Uma cana rachada e um pavio fumegante são coisas que normalmente se jogam fora. A frase descreve como o servo do Senhor vai tratá-las.",
 it="Una canna incrinata e uno stoppino che fuma appena sono cose che di solito si buttano via. La frase descrive come le tratterà il servo del Signore.",
 ko="상한 갈대와 꺼져 가는 등불은 보통 그냥 버리는 물건이다. 이 구절은 여호와의 종이 그것을 어떻게 다룰지 묘사한다."),
"isa-46-4": dict(
 pt="Dito em contraste com os ídolos babilônicos, carregados nos ombros nas festas. Aqui tudo se inverte: não é o deus que é carregado, mas a pessoa, e até os cabelos brancos.",
 it="Detto in contrasto con gli idoli babilonesi, portati a spalla durante le feste. Qui è l’inverso: non si porta il dio ma la persona, fino ai capelli bianchi.",
 ko="명절에 어깨에 메고 다니던 바벨론 우상과 대비하여 한 말이다. 여기서는 반대로 신이 아니라 사람이 업혀 가며, 백발이 되기까지 그렇다."),
"isa-49-15": dict(
 pt="Resposta a um povo que dizia ter sido esquecido. O profeta pega a comparação mais impossível que existe e diz que nem ela basta.",
 it="Risposta a un popolo che diceva di essere stato dimenticato. Il profeta prende il paragone più impossibile che ci sia e dice che perfino quello non basta.",
 ko="자기들이 잊혔다고 말하는 백성에게 주는 대답이다. 선지자는 가장 있을 수 없는 비유를 들고, 그것조차 모자란다고 말한다."),
"isa-50-4": dict(
 pt="De um cântico do servo. Saber sustentar o cansado é descrito como algo ensinado manhã após manhã, mais como um ofício do que como um dom.",
 it="Da un canto del servo del Signore. Saper sostenere chi è stanco è descritto come qualcosa che si impara mattina dopo mattina, più un mestiere che un dono.",
 ko="여호와의 종의 노래 가운데 하나다. 곤핍한 자를 말로 돕는 능력은 아침마다 배우는 것, 곧 타고난 재능이 아니라 기술처럼 묘사된다."),
"isa-54-10": dict(
 pt="Dito a um povo depois da catástrofe, num capítulo que chama Jerusalém de esposa abandonada. Os montes servem de imagem do que há de mais estável para uma pessoa.",
 it="Detto a un popolo dopo la catastrofe, in un capitolo che chiama Gerusalemme sposa abbandonata. I monti sono presi come immagine della cosa più stabile che si conosca.",
 ko="재앙을 겪은 백성에게 한 말로, 예루살렘을 버림받은 아내라 부르는 장에 있다. 산은 사람이 아는 가장 견고한 것의 상징으로 쓰였다."),
"isa-58-11": dict(
 pt="A promessa é condicional: antes vem a exigência de alimentar o faminto e abrigar o sem-teto. O jardim regado recompensa isso, não o jejum.",
 it="La promessa è condizionata: prima viene la richiesta di sfamare l’affamato e accogliere il senzatetto. Il giardino irrigato premia questo, non il digiuno.",
 ko="조건이 붙은 약속이다. 앞에 주린 자를 먹이고 집 없는 자를 들이라는 요구가 있다. 물 댄 동산은 금식이 아니라 그 일에 대한 보상이다."),
"jer-1-5": dict(
 pt="Jeremias responde que é jovem demais e não sabe falar. A tarefa para a qual é chamado vai durar quarenta anos e não lhe trará nenhum sucesso.",
 it="Geremia risponde di essere troppo giovane e di non saper parlare. Il compito a cui è chiamato durerà quarant’anni e non gli porterà alcun successo.",
 ko="예레미야는 자신이 아이라서 말할 줄 모른다고 대답한다. 그가 부름받은 사역은 사십 년 동안 이어지며 그에게 성공을 안겨 주지 않는다."),
"jer-6-16": dict(
 pt="Dito numa encruzilhada: o profeta aconselha parar e perguntar pelas veredas antigas. O texto diz que o povo respondeu que não andaria nelas.",
 it="Detto a un bivio: il profeta consiglia di fermarsi e chiedere dei sentieri antichi. Il testo dice che il popolo rispose che non li avrebbe percorsi.",
 ko="갈림길에서 한 말이다. 선지자는 멈춰 서서 옛적 길을 물어보라고 권한다. 본문에 따르면 백성은 그 길로 가지 않겠다고 대답했다."),
"jer-32-17": dict(
 pt="Jeremias ora sob guarda numa cidade sitiada, depois de comprar um campo que os babilônios estão prestes a ocupar.",
 it="Geremia prega sotto custodia in una città assediata, dopo aver appena comprato un campo che i Babilonesi stanno per occupare.",
 ko="예레미야가 포위된 성에서 갇힌 채 드리는 기도다. 그는 바벨론 군대가 곧 차지할 밭을 막 사들인 참이었다."),
"jer-33-3": dict(
 pt="Dito a um profeta preso no pátio da guarda, sem poder sair. A promessa trata de coisas que ele ainda não conhece.",
 it="Detto a un profeta rinchiuso nel cortile della guardia, senza poter uscire. La promessa riguarda cose che ancora non conosce.",
 ko="시위대 뜰에 갇혀 나갈 수 없는 선지자에게 한 말이다. 약속은 그가 아직 알지 못하는 일에 관한 것이다."),
"lam-3-26": dict(
 pt="Do lamento pela Jerusalém destruída. A palavra traduzida como “bom” está ao lado de “em silêncio”: o conselho é esperar sem palavras.",
 it="Dal lamento su Gerusalemme distrutta. La parola resa con «bene» sta accanto a «in silenzio»: il consiglio riguarda un’attesa senza parole.",
 ko="무너진 예루살렘을 두고 부른 애가에 나온다. “좋도다”라는 말이 “잠잠히” 곁에 놓여 있어, 말없이 기다리라는 권고가 된다."),
"ezk-34-16": dict(
 pt="Dito num capítulo em que os pastores são os governantes que alimentavam a si mesmos em vez do rebanho. A promessa vem para substituí-los, não como consolo genérico.",
 it="Detto in un capitolo in cui i pastori sono i capi che nutrivano sé stessi invece del gregge. La promessa arriva a sostituirli, non come consolazione generica.",
 ko="양 떼 대신 자기 배를 채운 통치자들을 목자라 부르는 장에 있다. 이 약속은 막연한 위로가 아니라 그들을 대신하는 일로 주어진다."),
"ezk-37-3": dict(
 pt="A pergunta é feita no meio de um vale cheio de ossos secos. Ezequiel não responde “sim”, mas “tu o sabes”, e é a única resposta honesta possível.",
 it="La domanda è posta in mezzo a una valle piena di ossa secche. Ezechiele non risponde «sì» ma «tu lo sai»: l’unica risposta onesta possibile.",
 ko="마른 뼈가 가득한 골짜기 한가운데서 받은 질문이다. 에스겔은 “예”가 아니라 “주께서 아시나이다”라고 답한다. 할 수 있는 유일하게 정직한 대답이다."),
"dan-6-10": dict(
 pt="O decreto já está assinado e a oração está proibida sob pena de morte por trinta dias. Daniel abre as janelas e ora como sempre, três vezes ao dia.",
 it="Il decreto è già firmato e per trenta giorni pregare è vietato, pena la morte. Daniele apre le finestre e prega come sempre, tre volte al giorno.",
 ko="삼십 일 동안 기도하면 죽인다는 조서에 이미 어인이 찍혔다. 다니엘은 창을 열고 평소처럼 하루 세 번 기도한다."),
"jol-2-13": dict(
 pt="Rasgar as roupas era o sinal aceito de luto, visível a todos. O profeta propõe, em vez disso, algo que ninguém vai ver.",
 it="Strapparsi le vesti era il segno di lutto riconosciuto, visibile a tutti. Il profeta propone invece qualcosa che nessuno vedrà.",
 ko="옷을 찢는 것은 누구나 볼 수 있는 통상적인 슬픔의 표시였다. 선지자는 그 대신 아무도 보지 못할 것을 제안한다."),
"amo-5-24": dict(
 pt="Dito a pessoas cujo culto estava em perfeita ordem. O profeta diz que não suporta ouvir seus cânticos e exige outra coisa no lugar.",
 it="Detto a persone il cui culto era in perfetto ordine. Il profeta dice di non sopportare di ascoltare i loro canti ed esige qualcos’altro.",
 ko="예배를 흠잡을 데 없이 드리던 사람들에게 한 말이다. 선지자는 그들의 노래를 듣기 싫다고 하며 다른 것을 요구한다."),
"jon-2-2": dict(
 pt="Jonas ora de dentro do peixe, onde foi parar fugindo de uma missão. Ele mesmo tinha pedido aos marinheiros que o jogassem ao mar.",
 it="Giona prega dal ventre del pesce, dove è finito fuggendo da un incarico. Era stato lui stesso a chiedere ai marinai di gettarlo in mare.",
 ko="요나가 물고기 뱃속에서 드리는 기도다. 맡은 일을 피해 달아나다 그곳에 이르렀다. 자기를 바다에 던지라고 선원들에게 청한 것도 그 자신이었다."),
"mic-7-8": dict(
 pt="Dito num capítulo em que o profeta se queixa de que não restou gente honesta e nem os da própria casa merecem confiança. A frase sobre cair vem depois disso.",
 it="Detto in un capitolo in cui il profeta lamenta che non restano persone oneste e che non ci si può fidare nemmeno dei familiari. La frase sulla caduta viene dopo.",
 ko="정직한 사람이 남지 않았고 집안 식구조차 믿을 수 없다고 선지자가 탄식하는 장에 있다. 넘어짐에 관한 구절은 그 뒤에 나온다."),
"nam-1-7": dict(
 pt="O livro inteiro trata da queda de Nínive, capital de um império que devastou metade do mundo conhecido. A frase sobre o refúgio está dentro dessa profecia.",
 it="Il libro parla interamente della caduta di Ninive, capitale di un impero che aveva devastato mezzo mondo conosciuto. La frase sul rifugio sta dentro questa profezia.",
 ko="이 책은 처음부터 끝까지 세상의 절반을 짓밟은 제국의 수도 니느웨의 멸망을 다룬다. 환난 날의 산성에 관한 구절은 그 예언 안에 있다."),
"hab-2-3": dict(
 pt="Resposta a um profeta que se pôs em seu posto e exigiu uma explicação. Ele recebe a ordem de escrever a visão em letras grandes, para ser lida por quem passa correndo.",
 it="Risposta a un profeta che si era messo di sentinella e chiedeva spiegazioni. Gli viene detto di scrivere la visione in grande, perché si legga anche correndo.",
 ko="파수하는 곳에 서서 설명을 요구한 선지자에게 주는 대답이다. 그는 달려가면서도 읽을 수 있게 묵시를 크게 새기라는 명을 받는다."),
"zec-4-6": dict(
 pt="Dito a um homem que precisa terminar um templo com um punhado de exilados que voltaram. Depois o profeta pergunta quem despreza o dia dos pequenos começos.",
 it="Detto a un uomo che deve finire un tempio con una manciata di esuli rientrati. Il profeta chiede poi chi disprezzi il giorno dei piccoli inizi.",
 ko="포로에서 돌아온 소수와 함께 성전을 완성해야 하는 사람에게 한 말이다. 선지자는 이어서 작은 일의 날을 멸시하는 자가 누구냐고 묻는다."),
"mal-3-10": dict(
 pt="O único lugar em que se convida a pôr à prova: o profeta diz “provai-me”. Dito a pessoas que traziam animais doentes como oferta.",
 it="L’unico punto in cui si invita a mettere alla prova: il profeta dice «mettetemi alla prova». Detto a gente che portava in offerta animali malati.",
 ko="시험해 보라고 권하는 유일한 대목으로, 선지자는 “나를 시험하여”라고 전한다. 병든 짐승을 제물로 바치던 사람들에게 한 말이다."),
"mat-4-4": dict(
 pt="Resposta à primeira tentação, depois de quarenta dias sem comer. Jesus cita Deuteronômio: palavras ditas a um povo também no deserto, também com fome.",
 it="Risposta alla prima tentazione, dopo quaranta giorni senza cibo. Gesù cita il Deuteronomio: parole dette a un popolo anch’esso nel deserto, anch’esso affamato.",
 ko="사십 일을 굶은 뒤 받은 첫 번째 시험에 대한 대답이다. 예수는 신명기를 인용하는데, 그 말씀 역시 광야의 백성에게 굶주림에 관해 한 말이었다."),
"mat-6-21": dict(
 pt="Do Sermão do Monte. A ordem é o inverso do esperado: o tesouro é apontado como causa e o coração como efeito, e não o contrário.",
 it="Dal Discorso della montagna. L’ordine è l’inverso di quello atteso: il tesoro è indicato come causa e il cuore come effetto, non viceversa.",
 ko="산상수훈에 나온다. 순서가 예상과 반대다. 보물이 원인, 마음이 결과로 제시되며 그 반대가 아니다."),
"mat-6-33": dict(
 pt="Está no meio de uma conversa sobre comida e roupa, dirigida a pessoas que tinham uma única capa. Não se trata de ambição, mas de sobrevivência.",
 it="Sta nel mezzo di un discorso sul cibo e sui vestiti, rivolto a persone che possedevano un solo mantello. Non parla di ambizione, ma di sussistenza.",
 ko="겉옷 한 벌뿐인 사람들에게 먹고 입는 문제를 말하는 가운데 나온다. 야망이 아니라 생계에 관한 이야기다."),
"mat-9-36": dict(
 pt="Dito sobre a multidão que Jesus viu ao percorrer as cidades. O verbo grego aqui indica uma contração física por dentro, não compaixão em geral.",
 it="Detto della folla che Gesù vide percorrendo le città. Il verbo greco indica qui una stretta fisica interiore, non una compassione generica.",
 ko="예수가 여러 성을 두루 다니며 본 무리에 관한 말이다. 여기 쓰인 헬라어 동사는 막연한 동정이 아니라 속이 물리적으로 조여드는 것을 뜻한다."),
"mat-14-27": dict(
 pt="Noite, meio do lago, o barco açoitado pelas ondas há horas. Os discípulos gritam de medo, achando que a figura que vem na direção deles é um fantasma.",
 it="Notte, in mezzo al lago, la barca sbattuta dalle onde da ore. I discepoli gridano di paura, scambiando per un fantasma la figura che si avvicina.",
 ko="밤, 호수 한가운데, 배는 몇 시간째 물결에 시달리고 있다. 제자들은 다가오는 이를 유령으로 여기고 무서워 소리친다."),
"mat-16-24": dict(
 pt="Dito depois que Pedro tentou dissuadi-lo de morrer. Os ouvintes viam cruzes à beira das estradas e entendiam a imagem ao pé da letra.",
 it="Detto dopo che Pietro aveva cercato di dissuaderlo dal morire. Gli ascoltatori vedevano croci lungo le strade e capivano l’immagine alla lettera.",
 ko="베드로가 그의 죽음을 말리려 한 뒤에 한 말이다. 듣는 이들은 길가에 선 십자가를 보아 왔기에 이 비유를 문자 그대로 이해했다."),
"mat-25-40": dict(
 pt="De uma cena de julgamento em que os dois lados ficam igualmente surpresos. Nenhum dos grupos sabia a quem de fato estava ajudando, ou deixando de ajudar.",
 it="Da una scena di giudizio in cui entrambe le parti sono ugualmente sorprese. Nessuno dei due gruppi sapeva chi avesse davvero aiutato, o non aiutato.",
 ko="양쪽 모두 똑같이 놀라는 심판 장면에서 나온다. 어느 쪽도 자기가 실제로 누구를 도왔는지, 누구를 돕지 않았는지 알지 못했다."),
"mat-26-39": dict(
 pt="Dito à noite num jardim, com o rosto em terra, horas antes da prisão. Pouco antes, ele diz aos discípulos que sua alma está triste até a morte.",
 it="Detto di notte in un giardino, con il volto a terra, poche ore prima dell’arresto. Poco prima dice ai discepoli che la sua anima è triste fino alla morte.",
 ko="체포되기 몇 시간 전, 밤에 동산에서 얼굴을 땅에 대고 한 말이다. 그 직전에 예수는 제자들에게 마음이 심히 고민하여 죽게 되었다고 말한다."),
"mrk-1-35": dict(
 pt="O dia anterior tinha sido longo, de curas, com a cidade inteira à porta até a noite. Ele se levanta antes do amanhecer e sai sozinho; os discípulos vão procurá-lo.",
 it="Il giorno prima era stato lungo, pieno di guarigioni, con tutta la città alla porta fino a notte. Si alza prima dell’alba e se ne va da solo; i discepoli lo cercano.",
 ko="전날은 온 동네가 밤까지 문 앞에 모인 긴 치유의 하루였다. 예수는 날이 밝기 전에 일어나 홀로 떠나고, 제자들이 그를 찾아 나선다."),
"mrk-4-39": dict(
 pt="Uma tempestade no lago, o barco se enchendo de água, e ele dormindo na popa. Os discípulos o acordam perguntando se não se importa que estejam se afogando.",
 it="Una tempesta sul lago, la barca si riempie d’acqua e lui dorme a poppa. I discepoli lo svegliano chiedendogli se non gli importa che stiano annegando.",
 ko="호수에 광풍이 일어 배에 물이 차는데, 예수는 고물에서 자고 있다. 제자들은 자기들이 죽게 된 것을 돌아보지 않느냐고 물으며 그를 깨운다."),
"mrk-5-34": dict(
 pt="Dito a uma mulher que sangrava havia doze anos. Pela lei, ela era impura e não tinha direito de tocar em ninguém; por isso chegou por trás.",
 it="Detto a una donna che perdeva sangue da dodici anni. Per la legge era impura e non poteva toccare nessuno: per questo si era avvicinata da dietro.",
 ko="열두 해 동안 혈루증을 앓은 여자에게 한 말이다. 율법상 그는 부정하여 누구도 만질 수 없었기에 뒤로 다가왔다."),
"mrk-6-31": dict(
 pt="Dito aos discípulos que voltavam da primeira viagem sozinhos. O motivo vem ali mesmo: era tanta gente indo e vindo que não tinham tempo nem para comer.",
 it="Detto ai discepoli tornati dal loro primo viaggio da soli. La ragione è spiegata subito: c’era così tanta gente che andava e veniva che non avevano il tempo di mangiare.",
 ko="처음으로 따로 보냄을 받았다가 돌아온 제자들에게 한 말이다. 이유도 바로 나온다. 오가는 사람이 많아 먹을 겨를도 없었다."),
"mrk-12-41": dict(
 pt="Jesus se senta diante da caixa das ofertas e observa as pessoas depositarem dinheiro. Ele não mede a quantia dada, mas quanto sobrou a quem deu.",
 it="Gesù siede di fronte al tesoro del tempio e guarda la gente versare denaro. Non misura quanto viene dato, ma quanto resta a chi dona.",
 ko="예수는 연보궤 맞은편에 앉아 사람들이 돈 넣는 것을 본다. 그는 넣은 액수가 아니라 넣은 뒤 그 사람에게 얼마가 남았는지를 본다."),
"luk-2-10": dict(
 pt="Dito a pastores num campo à noite: homens cujo trabalho os tornava ritualmente impuros e que não eram convidados a lugar nenhum.",
 it="Detto a pastori in un campo di notte: uomini che il loro lavoro rendeva ritualmente impuri e che nessuno invitava mai.",
 ko="밤 들판의 목자들에게 한 말이다. 그들은 하는 일 때문에 의식상 부정하게 여겨졌고 어디에도 초대받지 못했다."),
"luk-5-16": dict(
 pt="Quanto mais gente se juntava, mais vezes ele se retirava. Lucas registra isso não como exceção, mas como hábito constante.",
 it="Più la gente si radunava, più spesso lui si ritirava. Luca lo annota non come un’eccezione, ma come un’abitudine costante.",
 ko="사람들이 많이 모일수록 예수는 더 자주 물러갔다. 누가는 이것을 예외가 아니라 늘 있던 습관으로 기록한다."),
"luk-7-13": dict(
 pt="Dito a uma viúva que enterrava o filho único. Ela ficava sem nenhum homem em casa, o que naquela época significava a miséria.",
 it="Detto a una vedova che seppellisce il suo unico figlio. Restava senza alcun uomo in casa, cosa che a quel tempo significava miseria.",
 ko="외아들을 장사하러 가는 과부에게 한 말이다. 집안에 남자가 하나도 남지 않았으니, 당시로서는 곧 빈곤을 뜻했다."),
"luk-12-15": dict(
 pt="Resposta a um homem que lhe pediu para resolver uma disputa de herança com o irmão. Jesus se recusa a ser juiz e fala de algo completamente diferente.",
 it="Risposta a un uomo che gli chiedeva di risolvere con il fratello una lite sull’eredità. Gesù rifiuta di fare da giudice e parla di tutt’altro.",
 ko="형과 유산을 나누게 해 달라고 청한 사람에게 주는 대답이다. 예수는 재판장 노릇을 거절하고 전혀 다른 이야기를 한다."),
"luk-12-32": dict(
 pt="A expressão “pequeno rebanho” fala de tamanho: os ouvintes eram poucos e sabiam disso. Dito logo depois da conversa sobre comida e roupa.",
 it="L’espressione «piccolo gregge» riguarda le dimensioni: gli ascoltatori erano pochi e lo sapevano. Detto subito dopo il discorso sul cibo e sui vestiti.",
 ko="“적은 무리”라는 말은 규모를 가리킨다. 듣는 이는 적었고 스스로도 그것을 알았다. 먹고 입는 것에 관한 이야기 바로 뒤에 나온다."),
"luk-17-5": dict(
 pt="Os apóstolos pedem mais fé logo depois de ouvirem que devem perdoar sete vezes por dia. A resposta sobre o grão de mostarda fala de tamanho, não de quantidade.",
 it="Gli apostoli chiedono più fede subito dopo che è stato detto loro di perdonare sette volte al giorno. La risposta sul granello di senape riguarda la dimensione, non la quantità.",
 ko="하루에 일곱 번이라도 용서하라는 말을 들은 직후 사도들은 믿음을 더해 달라고 청한다. 겨자씨에 관한 대답은 양이 아니라 크기에 관한 것이다."),
"luk-18-1": dict(
 pt="Introdução a uma parábola sobre uma viúva que insistiu junto a um juiz corrupto até ele ceder. Lucas diz abertamente para que serve a parábola.",
 it="Introduzione a una parabola su una vedova che tornava di continuo da un giudice corrotto, finché lui non cedette. Luca dice apertamente a che cosa serve la parabola.",
 ko="불의한 재판관이 손들 때까지 찾아간 과부의 비유를 여는 말이다. 누가는 이 비유를 왜 말했는지 분명히 밝힌다."),
"luk-19-10": dict(
 pt="Dito na casa de Zaqueu, um cobrador de impostos que a cidade inteira considerava traidor. Lá fora, a multidão murmurava porque ele tinha entrado na casa de um homem assim.",
 it="Detto in casa di Zaccheo, un esattore delle tasse che tutta la città considerava un traditore. Fuori la folla mormorava che fosse entrato in casa di un uomo simile.",
 ko="온 성이 배신자로 여기던 세리 삭개오의 집에서 한 말이다. 밖에서는 무리가 그가 그런 사람의 집에 들어갔다고 수군거리고 있었다."),
"luk-24-32": dict(
 pt="Dois discípulos saíam de Jerusalém discutindo a execução e não reconheceram o companheiro de caminho. Só perceberam quem ele era depois que desapareceu.",
 it="Due discepoli uscivano da Gerusalemme parlando dell’esecuzione e non riconobbero il compagno di strada. Capirono chi era solo dopo che scomparve.",
 ko="두 제자는 처형된 일을 이야기하며 예루살렘을 떠나 걷다가 동행자를 알아보지 못했다. 그가 사라진 뒤에야 누구였는지 깨달았다."),
"jhn-4-14": dict(
 pt="Dito junto a um poço, ao meio-dia, a uma samaritana que vinha buscar água na hora mais quente para não encontrar as outras mulheres do povoado.",
 it="Detto presso un pozzo, a mezzogiorno, a una donna samaritana venuta ad attingere nell’ora più calda per non incontrare le altre donne del villaggio.",
 ko="한낮 우물가에서 사마리아 여자에게 한 말이다. 그는 마을 여자들을 마주치지 않으려고 가장 더운 시간에 물을 길으러 왔다."),
"jhn-6-35": dict(
 pt="Dito no dia seguinte a ter alimentado cinco mil pessoas. A multidão voltou, e ele diz sem rodeios que não procuram um sinal, mas comida.",
 it="Detto il giorno dopo che aveva sfamato cinquemila persone. La folla è tornata, e lui dice apertamente che non cercano un segno, ma cibo.",
 ko="오천 명을 먹인 다음 날 한 말이다. 무리가 다시 찾아오자 예수는 그들이 표적이 아니라 먹을 것을 찾는다고 분명히 말한다."),
"jhn-9-25": dict(
 pt="Dito por um homem cego de nascença, num interrogatório montado para arrancar dele uma resposta específica. Ele se recusa a discutir teologia e se atém ao que sabe.",
 it="Parla un uomo cieco dalla nascita, durante un interrogatorio pensato per strappargli una risposta precisa. Rifiuta di discutere di teologia e si attiene a ciò che sa.",
 ko="날 때부터 앞을 보지 못한 사람이 원하는 답을 받아 내려는 심문을 받으며 한 말이다. 그는 신학 논쟁을 거부하고 아는 것만 붙든다."),
"jhn-12-24": dict(
 pt="Dito dias antes da execução, quando alguns gregos pediram para vê-lo. A resposta não trata do encontro, mas do que precisa acontecer com ele.",
 it="Detto pochi giorni prima dell’esecuzione, quando alcuni Greci chiesero di vederlo. La sua risposta non riguarda l’incontro, ma ciò che deve accadere a lui.",
 ko="처형 며칠 전, 헬라인 몇 사람이 예수를 뵙고자 했을 때 한 말이다. 그의 대답은 만남이 아니라 자신에게 일어나야 할 일에 관한 것이다."),
"jhn-14-1": dict(
 pt="A primeira frase do discurso de despedida, dita logo depois de avisar Pedro sobre a negação. Nesse momento, os discípulos estão abalados.",
 it="La frase d’apertura del discorso d’addio, detta subito dopo aver avvertito Pietro del rinnegamento. In quel momento i discepoli sono scossi.",
 ko="고별 설교의 첫 문장으로, 베드로에게 부인할 것을 경고한 직후에 나온다. 그때 제자들은 크게 낙심해 있었다."),
"jhn-15-5": dict(
 pt="Dito a caminho do jardim, talvez passando por vinhas fora da cidade. A imagem era literal: um ramo separado da videira não dura nem um dia.",
 it="Detto lungo la strada verso il giardino, forse passando accanto alle vigne fuori città. L’immagine era letterale: un tralcio staccato dalla vite non dura un giorno.",
 ko="동산으로 가는 길에, 아마 성 밖 포도원 곁을 지나며 한 말이다. 이 비유는 문자 그대로 통했다. 나무에서 떨어진 가지는 하루도 못 간다."),
"jhn-16-22": dict(
 pt="Jesus compara o que está por vir a um parto: a dor não é anulada nem encurtada, mas deixa de ser o principal quando passa.",
 it="Gesù paragona ciò che sta per accadere al parto: il dolore non viene annullato né abbreviato, ma smette di essere la cosa principale quando è finito.",
 ko="예수는 다가올 일을 해산에 비유한다. 고통은 없어지지도 짧아지지도 않지만, 끝나고 나면 더 이상 중심이 아니다."),
"jhn-21-17": dict(
 pt="Pedro o negou três vezes junto a uma fogueira num pátio e agora é questionado três vezes junto a outra fogueira, na praia. A restauração corresponde ao número de negações.",
 it="Pietro lo aveva rinnegato tre volte vicino a un fuoco in un cortile, e ora viene interrogato tre volte vicino a un altro fuoco, sulla riva. Il conto corrisponde ai rinnegamenti.",
 ko="베드로는 뜰의 불 곁에서 세 번 부인했고, 이제 바닷가의 다른 숯불 곁에서 세 번 질문을 받는다. 회복은 부인한 횟수에 맞춰져 있다."),
"act-4-13": dict(
 pt="É assim que o Sinédrio, um conselho instruído que julgava o caso, descreve Pedro e João. A palavra não quer dizer tolos, mas sem estudo.",
 it="Così il sinedrio, un consiglio di persone istruite che esaminava il loro caso, descrive Pietro e Giovanni. La parola non significa stupidi, ma privi di istruzione scolastica.",
 ko="베드로와 요한의 일을 심리하던 학식 있는 공회가 두 사람을 이렇게 평한다. 이 말은 어리석다는 뜻이 아니라 학교에서 배우지 않았다는 뜻이다."),
"act-16-25": dict(
 pt="Paulo e Silas tinham sido açoitados com varas e trancados na prisão interior, com os pés no tronco. É meia-noite, e os outros presos estão ouvindo.",
 it="Paolo e Sila erano stati bastonati e chiusi nella prigione più interna, con i piedi nei ceppi. È mezzanotte, e gli altri prigionieri ascoltano.",
 ko="바울과 실라는 매를 맞고 깊은 옥에 갇혀 발에 착고가 채워졌다. 한밤중이고, 다른 죄수들이 듣고 있다."),
"act-17-28": dict(
 pt="Paulo fala em Atenas diante de filósofos e cita não as Escrituras, mas um poeta grego, porque esses ouvintes nunca tinham lido as Escrituras.",
 it="Paolo parla ad Atene davanti a filosofi e cita non la Scrittura ma un poeta greco, perché quegli ascoltatori non avevano mai letto le Scritture.",
 ko="바울은 아덴에서 철학자들 앞에 서서 성경이 아니라 헬라 시인을 인용한다. 이 청중은 성경을 읽어 본 적이 없었기 때문이다."),
"rom-3-23": dict(
 pt="Conclusão de um longo raciocínio em que Paulo mostrou que gentios e judeus estão na mesma situação. O “todos” aqui é o resultado de uma demonstração.",
 it="Conclusione di un lungo ragionamento in cui Paolo ha mostrato che pagani ed ebrei sono nella stessa condizione. La parola «tutti» qui è il risultato di una dimostrazione.",
 ko="이방인과 유대인이 같은 처지에 있음을 보인 긴 논증의 결론이다. 여기서 “모든”이라는 말은 증명의 결과다."),
"rom-8-1": dict(
 pt="Vem logo depois de um capítulo em que Paulo descreve fazer o que não quer e se chama de homem miserável. Esta é a resposta a esse grito.",
 it="Viene subito dopo un capitolo in cui Paolo descrive di fare ciò che non vuole e si definisce un uomo infelice. È la risposta a quel grido.",
 ko="원하지 않는 일을 행한다고 고백하며 자신을 곤고한 사람이라 부른 장 바로 뒤에 나온다. 이 구절은 그 부르짖음에 대한 대답이다."),
"rom-8-26": dict(
 pt="Dito sobre a situação em que a pessoa não sabe o que pedir. Paulo não aconselha encontrar as palavras; diz que talvez não haja palavra nenhuma.",
 it="Detto della situazione in cui non si sa che cosa chiedere. Paolo non consiglia di trovare le parole: dice che le parole possono mancare del tutto.",
 ko="무엇을 구해야 할지 모르는 상황에 관한 말이다. 바울은 알맞은 말을 찾으라고 권하지 않고, 말이 아예 없을 수도 있다고 말한다."),
"rom-8-38": dict(
 pt="Fim de um capítulo que começou com a ausência de condenação. Paulo enumera tudo o que lhe vem à mente, inclusive a morte e o futuro, e encerra a lista.",
 it="La fine di un capitolo iniziato con l’assenza di condanna. Paolo elenca tutto ciò che gli viene in mente, compresi la morte e il futuro, e chiude l’elenco.",
 ko="정죄함이 없다는 말로 시작한 장의 끝이다. 바울은 죽음과 장래 일을 포함해 떠오르는 모든 것을 열거하고 목록을 닫는다."),
"rom-12-15": dict(
 pt="De uma lista de instruções curtas. A ordem importa: alegrar-se com os que se alegram vem primeiro, e costuma ser mais difícil do que chorar com os que choram.",
 it="Da un elenco di brevi istruzioni. L’ordine conta: prima viene rallegrarsi con chi si rallegra, cosa di solito più difficile che piangere con chi piange.",
 ko="짧은 권면들을 늘어놓은 목록에 있다. 순서가 중요하다. 즐거워하는 자와 함께 즐거워하는 일이 먼저이고, 대개 우는 자와 함께 우는 것보다 어렵다."),
"rom-12-21": dict(
 pt="Conclusão de uma seção sobre como tratar os inimigos. Logo antes, Paulo cita Provérbios e fala de comida e bebida para o adversário.",
 it="Conclusione di una sezione su come trattare i nemici. Poco prima Paolo cita i Proverbi e parla di cibo e bevande per l’avversario.",
 ko="원수를 어떻게 대할지 다룬 단락의 결론이다. 바로 앞에서 바울은 잠언을 인용하며 원수에게 먹을 것과 마실 것을 주라고 말한다."),
"1co-1-27": dict(
 pt="Paulo lembra aos coríntios como era a própria comunidade: não muitos sábios, não muitos de nobre nascimento. Diz isso a uma comunidade orgulhosa da própria espiritualidade.",
 it="Paolo ricorda ai Corinzi chi sono: non molti sapienti, non molti di nobile nascita. Lo dice a una comunità fiera della propria spiritualità.",
 ko="바울은 고린도 교인들에게 그들의 면면을 상기시킨다. 지혜 있는 자도, 문벌 좋은 자도 많지 않았다. 자기들의 영성을 자랑하던 공동체에 한 말이다."),
"1co-15-58": dict(
 pt="A última frase do capítulo sobre a ressurreição, o argumento mais longo de Paulo de que a morte não é definitiva. A conclusão acaba sendo sobre o trabalho.",
 it="L’ultima riga del capitolo sulla risurrezione, il ragionamento più lungo di Paolo sul fatto che la morte non è definitiva. La conclusione finisce per riguardare il lavoro.",
 ko="죽음이 끝이 아님을 논한 바울의 가장 긴 논증, 부활 장의 마지막 구절이다. 그 결론은 뜻밖에도 일에 관한 것이다."),
"2co-9-7": dict(
 pt="De uma carta sobre uma coleta para os famintos de Jerusalém. Paulo passou anos reunindo-a e ressalta que a obrigação estraga tudo.",
 it="Da una lettera su una colletta per gli affamati di Gerusalemme. Paolo ha passato anni a raccoglierla e sottolinea che la costrizione rovina tutto.",
 ko="예루살렘의 굶주린 이들을 위한 연보에 관한 편지에 나온다. 바울은 여러 해 동안 이 연보를 모았고, 억지로 하면 모든 것이 망가진다고 강조한다."),
"2co-12-10": dict(
 pt="Conclusão do seu relato sobre uma fraqueza que não lhe foi tirada. Paulo enumera insultos e perseguições como coisas em que sente prazer.",
 it="Conclusione del suo racconto su una debolezza che non gli fu tolta. Paolo elenca offese e persecuzioni come condizioni in cui accetta volentieri di trovarsi.",
 ko="끝내 거두어지지 않은 약함에 관한 이야기의 결론이다. 바울은 능욕과 핍박을 기꺼이 머물 자리로 열거한다."),
"gal-3-28": dict(
 pt="Escrito num mundo em que essas três distinções decidiam tudo: direitos, tribunais, herança. Paulo nomeia exatamente as fronteiras que não podiam ser cruzadas.",
 it="Scritto in un mondo in cui quelle tre distinzioni decidevano tutto: diritti, tribunali, eredità. Paolo nomina proprio i confini che erano invalicabili.",
 ko="이 세 가지 구분이 권리와 재판과 상속을 모두 좌우하던 세상에서 쓴 글이다. 바울은 넘을 수 없던 바로 그 경계들을 꼽는다."),
"gal-6-2": dict(
 pt="Está ao lado de uma frase que diz que cada um levará o próprio fardo. As palavras gregas são diferentes: uma é um peso esmagador; a outra, a bagagem de um viajante.",
 it="Sta accanto a una frase che dice che ciascuno porterà il proprio carico. Le parole greche sono diverse: una indica un peso schiacciante, l’altra il bagaglio di un viaggiatore.",
 ko="각각 자기의 짐을 지리라는 구절 곁에 있다. 원어로는 두 단어가 다르다. 하나는 짓누르는 무거운 짐, 다른 하나는 길 가는 사람의 봇짐이다."),
"eph-4-2": dict(
 pt="Início da metade prática da carta. A palavra traduzida como “suportando-vos” significa aguentar uma pessoa incômoda, não perdoar uma ofensa.",
 it="L’inizio della parte pratica della lettera. La parola resa con «sopportandovi» significa tollerare una persona scomoda, non perdonare un’offesa.",
 ko="편지의 실천적인 후반부가 시작되는 곳이다. “용납하고”로 번역된 말은 잘못을 용서하는 것이 아니라 불편한 사람을 견디는 것을 뜻한다."),
"eph-4-26": dict(
 pt="A ira não é proibida aqui; recebe um prazo. A medida vem do próprio dia: o pôr do sol era o fim do dia, não uma figura de linguagem.",
 it="Qui l’ira non è vietata: le si fissa un limite di tempo. La misura viene dal giorno stesso: il tramonto era la fine della giornata, non una figura retorica.",
 ko="분노 자체는 금지되지 않고 기한이 정해진다. 그 척도는 하루에서 왔다. 해 지는 것은 비유가 아니라 실제 하루의 끝이었다."),
"eph-5-15": dict(
 pt="A expressão traduzida como “remindo o tempo” significa literalmente comprar o tempo de volta, como se compram mercadorias no mercado, porque os dias são maus.",
 it="L’espressione resa con «facendo buon uso del tempo» significa letteralmente riscattare il tempo, come si compra una merce al mercato, perché i giorni sono cattivi.",
 ko="“세월을 아끼라”로 번역된 표현은 본래 시장에서 물건을 사듯 시간을 되사라는 뜻이다. 때가 악하기 때문이다."),
"php-3-13": dict(
 pt="Paulo acaba de enumerar seu passado, inclusive a perseguição à igreja, e chamar tudo de lixo. O esquecimento aqui abrange tanto seus méritos quanto sua culpa.",
 it="Paolo ha appena elencato il suo passato, compresa la persecuzione della Chiesa, e l’ha chiamato tutto spazzatura. Qui dimenticare riguarda sia i suoi meriti sia la sua colpa.",
 ko="바울은 교회를 핍박한 일까지 포함해 자기 과거를 늘어놓고 모두 배설물로 여긴다고 했다. 여기서 잊는 것은 자기 공로와 자기 죄책 둘 다다."),
"php-4-11": dict(
 pt="Paulo ressalta que aprendeu a estar contente, e não que já começou contente. Ele cita as duas escolas pelas quais passou: a fartura e a fome.",
 it="Paolo sottolinea di aver imparato ad accontentarsi, non di esserne capace fin dall’inizio. Nomina entrambe le scuole che ha attraversato: la sazietà e la fame.",
 ko="바울은 처음부터 자족한 것이 아니라 자족하기를 배웠다고 강조한다. 그는 거쳐 온 두 학교, 배부름과 배고픔을 모두 꼽는다."),
"col-3-15": dict(
 pt="O verbo traduzido como “seja o árbitro” vem do esporte: descrevia o juiz que concedia o prêmio. A paz é instalada como juíza dentro da pessoa.",
 it="Il verbo reso con «regni» viene dallo sport: indicava l’arbitro che assegna il premio. La pace è posta come arbitro dentro la persona.",
 ko="“주장하게 하라”로 번역된 동사는 경기에서 상을 판정하는 심판을 가리키던 말이다. 평강이 사람 안의 심판으로 세워진다."),
"col-4-6": dict(
 pt="O sal, naquele mundo, era conservante e medida de valor, não um tempero para dar picância. A ideia é que as palavras não se estraguem.",
 it="In quel mondo il sale era un conservante e una misura di valore, non un condimento per dare sapore piccante. Il punto è che le parole non si guastino.",
 ko="그 시대에 소금은 톡 쏘는 양념이 아니라 방부제이자 가치의 척도였다. 요점은 말이 상하지 않게 하라는 것이다."),
"1th-5-11": dict(
 pt="Dito a uma comunidade que esperava o fim a qualquer dia e estava inquieta por isso. A instrução é simples: continuem fazendo o que já fazem.",
 it="Detto a una comunità che aspettava la fine da un giorno all’altro e per questo era in agitazione. L’indicazione è semplice: continuate a fare ciò che già fate.",
 ko="종말이 당장이라도 올 줄 알고 초조해하던 공동체에 한 말이다. 지시는 단순하다. 이미 하고 있는 대로 계속하라는 것이다."),
"1ti-4-12": dict(
 pt="Escrito a Timóteo, deixado em Éfeso à frente de uma comunidade, sendo visivelmente mais jovem que as pessoas que liderava.",
 it="Scritto a Timoteo, rimasto a Efeso a guidare una comunità pur essendo nettamente più giovane di coloro che guidava.",
 ko="에베소에 남아 공동체를 이끌던 디모데에게 쓴 글이다. 그는 자기가 이끄는 사람들보다 눈에 띄게 젊었다."),
"1ti-6-6": dict(
 pt="Dito numa seção sobre pessoas que tratam a piedade como meio de ganhar dinheiro. A medida do suficiente é comida e roupa, e nada mais.",
 it="Detto in una sezione su persone che considerano la pietà un modo per guadagnare. Come misura del necessario sono indicati cibo e vestiti, e nient’altro.",
 ko="경건을 이익의 수단으로 여기는 사람들에 관한 단락에 있다. 족함의 기준으로 제시된 것은 먹을 것과 입을 것뿐이다."),
"2ti-4-7": dict(
 pt="As últimas linhas da última carta de Paulo. Pouco depois, no versículo 13, ele pede a capa que deixou em Trôade: o balanço final fica entre pedidos domésticos.",
 it="Le ultime righe dell’ultima lettera di Paolo. Poco dopo, al versetto 13, chiede il mantello lasciato a Troas: il bilancio sta in mezzo a richieste quotidiane.",
 ko="바울의 마지막 편지 끝부분이다. 조금 뒤 13절에서 그는 드로아에 두고 온 겉옷을 가져오라고 부탁한다. 인생의 결산이 일상적인 부탁들 사이에 놓여 있다."),
"heb-6-19": dict(
 pt="Aqui a âncora não é lançada para baixo, mas para cima, para trás do véu do templo. A imagem é invertida de propósito em relação à náutica.",
 it="Qui l’àncora non è gettata verso il basso ma verso l’alto, dietro il velo del tempio. L’immagine è volutamente capovolta rispetto a quella marinara.",
 ko="여기서 닻은 아래가 아니라 위로, 성소의 휘장 안으로 던져진다. 배의 닻과는 일부러 뒤집어 놓은 이미지다."),
"heb-10-24": dict(
 pt="Dito a uma comunidade em que algumas pessoas já tinham deixado de ir às reuniões. O verbo traduzido como “estimular” significa provocar, uma palavra bem afiada.",
 it="Detto a una comunità in cui alcuni avevano già smesso di venire alle riunioni. Il verbo reso con «stimolare» significa provocare, una parola piuttosto forte.",
 ko="이미 모임에 나오지 않기 시작한 사람들이 있던 공동체에 한 말이다. “격려하며”로 번역된 동사는 “자극하다”에 가까운 꽤 날카로운 말이다."),
"heb-12-11": dict(
 pt="O autor admite abertamente que, no momento, a disciplina não parece agradável, e não tenta argumentar o contrário. Do fruto se fala no futuro.",
 it="L’autore ammette apertamente che sul momento non sembra piacevole, e non cerca di sostenere il contrario. Del frutto si parla al futuro.",
 ko="저자는 그 당시에는 즐겁지 않아 보인다고 솔직히 인정하고, 달리 설득하려 하지 않는다. 열매는 미래형으로 말한다."),
"jas-1-17": dict(
 pt="Uma imagem astronômica: os astros têm fases e eclipses, e Tiago diz que aqui não há nada disso. A comparação é mais precisa do que parece.",
 it="Un’immagine astronomica: i corpi celesti hanno fasi ed eclissi, e Giacomo dice che qui non ce ne sono. Il paragone è più preciso di quanto sembri.",
 ko="천문학적인 이미지다. 천체는 차고 기울며 가려지기도 하지만, 야고보는 여기에는 그런 것이 없다고 말한다. 들리는 것보다 정확한 비교다."),
"jas-1-19": dict(
 pt="Três instruções em ordem de dificuldade. Tiago escreve a uma comunidade em que, a julgar pela carta, as discussões eram frequentes e animadas.",
 it="Tre indicazioni in ordine di difficoltà. Giacomo scrive a una comunità in cui, a giudicare dalla lettera, si discuteva spesso e volentieri.",
 ko="어려운 순서대로 놓인 세 가지 권면이다. 편지로 미루어 보면, 야고보가 편지한 공동체는 논쟁이 잦고 열띠었다."),
"jas-4-14": dict(
 pt="Dito sobre pessoas que planejavam um ano de viagens e lucros pela frente. Tiago não proíbe planejar; ele se opõe à certeza sobre o amanhã.",
 it="Detto di persone che pianificano un anno di viaggi e guadagni. Giacomo non vieta di fare progetti: contesta la certezza sul domani.",
 ko="일 년 동안 다니며 장사해 이익을 보겠다고 계획하는 사람들에 관한 말이다. 야고보는 계획을 금하지 않고, 내일을 장담하는 것을 반대한다."),
"1pe-1-3": dict(
 pt="Início de uma carta a cristãos chamados de estrangeiros em suas próprias cidades. A esperança é chamada de viva, em contraste com uma herança que pode se perder.",
 it="L’inizio di una lettera a cristiani definiti stranieri nelle loro stesse città. La speranza è detta viva, a differenza di un’eredità che si può perdere.",
 ko="자기 고을에서조차 나그네라 불린 그리스도인들에게 보낸 편지의 첫머리다. 소망은 잃을 수 있는 유산과 대비되어 산 소망이라 불린다."),
"1pe-3-15": dict(
 pt="Dito a pessoas que podiam ser chamadas a interrogatório. A exigência de dar uma resposta vem junto com a de fazê-lo com mansidão, não com ar de triunfo.",
 it="Detto a persone che potevano essere convocate per un interrogatorio. La richiesta di rispondere va insieme a quella di farlo con mitezza, non con aria trionfante.",
 ko="심문에 불려 갈 수도 있던 사람들에게 한 말이다. 대답하라는 요구는 의기양양하게가 아니라 온유하게 하라는 요구와 함께 주어진다."),
"1pe-5-10": dict(
 pt="Pedro escreve “depois de terdes sofrido por um pouco”, sem prometer que não haverá sofrimento. O “pouco” é sua própria avaliação, feita de dentro da perseguição.",
 it="Pietro scrive «dopo che avrete un poco sofferto», senza promettere che la sofferenza non ci sarà. Quel «poco» è una sua valutazione, data dall’interno della persecuzione.",
 ko="베드로는 고난이 없으리라 약속하지 않고 “잠간 고난을 받은”이라고 쓴다. “잠간”은 박해 한가운데서 내린 그 자신의 평가다."),
"2pe-3-9": dict(
 pt="Resposta a quem perguntava onde está a vinda prometida, já que nada acontece. A demora não é explicada por esquecimento, mas por intenção.",
 it="Risposta a chi chiedeva dove fosse la venuta promessa, visto che non succedeva nulla. Il ritardo non è spiegato con la dimenticanza, ma con un’intenzione.",
 ko="아무 일도 일어나지 않는데 약속된 강림이 어디 있느냐고 묻는 이들에게 주는 대답이다. 지체는 잊어버림이 아니라 의도로 설명된다."),
"1jn-3-1": dict(
 pt="O verbo que abre a frase é uma exclamação: “vede”. João escreve a uma comunidade da qual alguns tinham saído e explica aos que ficaram quem eles são.",
 it="Il verbo che apre la frase è un’esclamazione: «guardate». Giovanni scrive a una comunità da cui alcuni se n’erano andati, e spiega a chi è rimasto chi sono.",
 ko="구절을 여는 동사는 “보라”라는 외침이다. 요한은 일부가 떠나 버린 공동체에 편지하며, 남은 이들에게 그들이 누구인지 설명한다."),
"1jn-3-18": dict(
 pt="Logo antes vem a pergunta sobre quem vê um irmão passando necessidade e lhe fecha o coração. A exigência de agir chega como resposta a essa pergunta.",
 it="Poco prima c’è la domanda su chi vede un fratello nel bisogno e gli chiude il cuore. La richiesta di agire arriva come risposta a quella domanda.",
 ko="바로 앞에 형제의 궁핍함을 보고도 마음을 닫는 사람에 관한 질문이 있다. 행함으로 하라는 요구는 그 질문에 대한 대답이다."),
"1jn-4-19": dict(
 pt="Uma frase curta sobre a ordem: o nosso não é o primeiro. Está logo depois das palavras sobre o medo expulso pelo amor.",
 it="Una frase breve sull’ordine: il nostro amore non viene per primo. Sta subito dopo le parole sulla paura scacciata dall’amore.",
 ko="순서에 관한 짧은 구절이다. 우리 사랑이 먼저가 아니다. 사랑이 두려움을 내쫓는다는 말 바로 뒤에 나온다."),
"rev-2-10": dict(
 pt="Carta à igreja de Esmirna, uma das duas, com Filadélfia, que não recebem nenhuma repreensão. O que lhes é prometido não é livramento, mas prisão e dez dias de tribulação.",
 it="Lettera alla chiesa di Smirne, una delle due, con Filadelfia, che non ricevono alcun rimprovero. Ciò che viene loro promesso non è la liberazione, ma il carcere e dieci giorni di tribolazione.",
 ko="빌라델비아와 함께 책망을 하나도 받지 않은 두 교회 중 하나인 서머나 교회에 보낸 편지다. 그들에게 약속된 것은 구출이 아니라 옥과 십 일 동안의 환난이다."),
"rev-21-5": dict(
 pt="Uma das poucas frases do livro ditas diretamente por aquele que está no trono. O prometido não são coisas novas, mas a renovação de tudo o que existe.",
 it="Una delle poche frasi del libro pronunciate direttamente da colui che siede sul trono. Ciò che è promesso non sono cose nuove, ma il rinnovamento di tutto ciò che esiste.",
 ko="보좌에 앉으신 이가 직접 하는 몇 안 되는 말 가운데 하나다. 약속된 것은 새로운 물건들이 아니라 존재하는 모든 것의 새로워짐이다."),
"gen-4-9": dict(
 pt="Caim responde a uma pergunta com outra, depois de já ter matado o irmão. Sua contrapergunta, se ele é o guardador do irmão, nunca recebe resposta direta na Bíblia.",
 it="Caino risponde a una domanda con una domanda, dopo aver già ucciso il fratello. La sua controdomanda, «sono forse il custode di mio fratello?», nella Bibbia non riceve mai risposta diretta.",
 ko="이미 아우를 죽인 가인이 질문에 질문으로 답한다. “내가 내 아우를 지키는 자니이까”라는 그의 반문은 성경에서 끝내 직접적인 답을 얻지 않는다."),
"gen-18-14": dict(
 pt="Dito depois que Sara riu atrás da parede da tenda ao ouvir falar do filho. Ela tem noventa anos e riu por dentro, não em voz alta.",
 it="Detto dopo che Sara aveva riso dietro la parete della tenda, sentendo parlare di un figlio. Ha novant’anni, e ha riso dentro di sé, non ad alta voce.",
 ko="아들 소식을 듣고 사라가 장막 문 뒤에서 웃은 뒤에 한 말이다. 그는 아흔 살이었고, 소리 내어서가 아니라 속으로 웃었다."),
"exo-4-11": dict(
 pt="Resposta a Moisés, que já tinha recusado quatro vezes alegando ser lento no falar. Depois disso, ele recusa pela quinta vez.",
 it="Risposta a Mosè, che si era rifiutato quattro volte adducendo di essere impacciato nel parlare. Dopo questo, rifiuta una quinta volta.",
 ko="네 번이나 거절하며 입이 뻣뻣하고 혀가 둔하다고 한 모세에게 주는 대답이다. 이 뒤에 그는 다섯 번째로 거절한다."),
"exo-17-12": dict(
 pt="Enquanto Moisés mantinha as mãos erguidas, a batalha pendia para Israel, mas suas mãos ficaram pesadas. Arão e Hur simplesmente puseram uma pedra debaixo dele e sustentaram seus braços.",
 it="Finché Mosè teneva alzate le mani, Israele prevaleva, ma le mani gli si fecero pesanti. Aronne e Cur gli misero semplicemente sotto una pietra e gli sostennero le braccia.",
 ko="모세가 손을 들고 있으면 이스라엘이 이겼지만, 그의 팔이 피곤해졌다. 아론과 훌은 그저 돌을 가져다 앉히고 그의 손을 붙들었다."),
"num-11-14": dict(
 pt="Moisés diz isso enquanto o povo chora pedindo carne. Em seguida, pede abertamente que o matem se aquilo continuar, e isso fica registrado sem atenuação.",
 it="Mosè lo dice mentre il popolo piange perché vuole carne. Poi chiede apertamente di essere ucciso se le cose continuano così, e questo è riportato senza attenuazioni.",
 ko="백성이 고기를 달라고 울 때 모세가 한 말이다. 이어서 그는 이대로라면 차라리 자기를 죽여 달라고 대놓고 청하며, 이 말은 누그러뜨리지 않고 기록되었다."),
"deu-4-29": dict(
 pt="Dito para o caso de o povo já estar espalhado entre outras nações. A promessa é feita de antemão, para o pior desfecho previsto.",
 it="Detto per il caso in cui il popolo sarà già disperso tra altre nazioni. La promessa è data in anticipo, per il peggiore degli esiti previsti.",
 ko="백성이 이미 여러 민족 가운데 흩어졌을 경우를 두고 한 말이다. 약속은 예상되는 가장 나쁜 결말에 대비해 미리 주어진다."),
"jos-14-11": dict(
 pt="Dito por Calebe aos oitenta e cinco anos, pedindo não um terreno tranquilo, mas a região montanhosa onde vivem os gigantes.",
 it="Parla Caleb a ottantacinque anni, chiedendo non un lotto tranquillo, ma la regione montuosa dove vivono i giganti.",
 ko="여든다섯 살의 갈렙이 한 말이다. 그는 편안한 땅이 아니라 거인 아낙 사람들이 사는 산지를 달라고 한다."),
"jdg-16-28": dict(
 pt="A última oração de Sansão: cego, de cabeça raspada e exposto à zombaria. Antes, o livro registra só uma oração dele, quando estava morrendo de sede.",
 it="L’ultima preghiera di Sansone, accecato, rasato ed esposto allo scherno. Prima il libro ne riporta una sola, quando stava morendo di sete.",
 ko="눈이 뽑히고 머리털이 밀린 채 조롱거리로 세워진 삼손의 마지막 기도다. 이 책에서 그 전에 나오는 그의 기도는 목말라 죽게 되었을 때 한 번뿐이다."),
"1sa-1-15": dict(
 pt="Ana se defende diante de um sacerdote que a julgou embriagada: ela orava em silêncio, movendo só os lábios. Naquela época não se orava assim.",
 it="Anna si difende davanti a un sacerdote che l’ha presa per ubriaca: pregava in silenzio, muovendo solo le labbra. A quel tempo non si pregava così.",
 ko="한나가 자기를 술 취한 줄 안 제사장에게 해명한다. 그는 입술만 움직이며 소리 없이 기도하고 있었다. 당시에는 그렇게 기도하지 않았다."),
"1sa-7-12": dict(
 pt="Samuel ergue uma pedra e lhe dá o nome de “pedra de ajuda”. O marco não é posto depois de uma vitória em geral, mas num ponto específico.",
 it="Samuele erige una pietra e la chiama «pietra dell’aiuto». Il segno non è posto dopo una vittoria in generale, ma in un luogo preciso.",
 ko="사무엘이 돌을 세우고 “도움의 돌”이라는 뜻의 에벤에셀이라 이름한다. 이 기념비는 승리 일반이 아니라 특정한 한 장소에 세워졌다."),
"2sa-9-7": dict(
 pt="Davi diz isso ao neto de Saul, o homem que o perseguiu durante anos. Mefibosete é aleijado dos dois pés e vive na casa de outra pessoa.",
 it="Davide lo dice al nipote di Saul, l’uomo che gli aveva dato la caccia per anni. Mefiboset è zoppo da entrambi i piedi e vive in casa d’altri.",
 ko="다윗이 여러 해 동안 자기 목숨을 노렸던 사울의 손자에게 하는 말이다. 므비보셋은 두 발을 다 절며 남의 집에 얹혀 살고 있다."),
"1ki-3-9": dict(
 pt="Salomão é convidado a pedir o que quiser e não pede riqueza nem vida longa, mas a capacidade de discernir entre as coisas. Ele tinha uns vinte anos.",
 it="A Salomone viene offerto tutto ciò che chiede, e lui non chiede ricchezza né lunga vita, ma la capacità di discernere. Aveva circa vent’anni.",
 ko="무엇이든 구하라는 말을 듣고 솔로몬은 부나 장수가 아니라 분별하는 능력을 구한다. 그는 그때 스무 살쯤이었다."),
"1ki-17-16": dict(
 pt="A viúva de Sarepta preparava um último pão para si e para o filho, para comê-lo e morrer. A farinha e o azeite não acabaram até o fim da seca.",
 it="La vedova di Sarepta stava preparando un’ultima focaccia per sé e per il figlio, per mangiarla e poi morire. La farina e l’olio non si esaurirono finché durò la siccità.",
 ko="사르밧의 과부는 아들과 함께 마지막 떡을 만들어 먹고 죽으려던 참이었다. 가루와 기름은 가뭄이 끝날 때까지 떨어지지 않았다."),
"1ki-19-4": dict(
 pt="Elias pede para morrer debaixo de um arbusto no deserto, no dia seguinte à maior vitória da sua vida. A resposta que recebe é comida e sono.",
 it="Elia chiede di morire sotto un arbusto nel deserto, il giorno dopo la più grande vittoria della sua vita. La risposta che riceve sono cibo e sonno.",
 ko="엘리야는 생애 최대의 승리를 거둔 다음 날, 광야의 로뎀 나무 아래서 죽기를 구한다. 그가 받은 대답은 음식과 잠이었다."),
"2ki-4-26": dict(
 pt="A mulher responde “está tudo bem”, embora seu único filho tenha morrido em seus braços naquela manhã. Ela não contou a ninguém até chegar ao profeta.",
 it="La donna risponde «tutto bene», anche se quella mattina il suo unico figlio le è morto tra le braccia. Non l’ha detto a nessuno prima di arrivare dal profeta.",
 ko="외아들이 그날 아침 품에서 죽었는데도 여인은 “평안하다”고 대답한다. 그는 선지자에게 이를 때까지 아무에게도 말하지 않았다."),
"1ch-28-20": dict(
 pt="Davi entrega a Salomão as plantas de um templo que ele mesmo não teve permissão de construir. Diz isso ao filho sabendo que não verá a obra.",
 it="Davide consegna a Salomone i progetti di un tempio che a lui non fu concesso di costruire. Lo dice al figlio sapendo che non vedrà i lavori.",
 ko="다윗이 자기는 짓지 못하게 된 성전의 설계도를 솔로몬에게 넘겨준다. 그는 그 공사를 보지 못할 것을 알면서 아들에게 이 말을 한다."),
"2ch-16-9": dict(
 pt="Dito ao rei Asa como repreensão: ele contratou um aliado em vez de confiar em Deus, e é acusado não de fracasso, mas de cálculo.",
 it="Detto al re Asa come rimprovero: aveva assoldato un alleato invece di affidarsi a Dio, ed è accusato non di un fallimento, ma di un calcolo.",
 ko="아사 왕을 책망하며 한 말이다. 그는 여호와를 의지하지 않고 동맹을 돈으로 샀으며, 실패가 아니라 계산한 것 때문에 책망받는다."),
"neh-1-4": dict(
 pt="Neemias é copeiro do rei persa e acaba de saber que os muros de Jerusalém estão em ruínas. Ele chorou e jejuou por dias antes de fazer qualquer coisa.",
 it="Neemia è coppiere del re di Persia e ha appena saputo che le mura di Gerusalemme sono in rovina. Pianse e digiunò per giorni prima di fare qualcosa.",
 ko="느헤미야는 바사 왕의 술 맡은 관원으로, 예루살렘 성벽이 무너졌다는 소식을 막 들었다. 그는 무엇을 하기 전에 여러 날 울며 금식했다."),
"est-4-16": dict(
 pt="Ester decide ir ao rei sem ter sido chamada, conhecendo a lei. Suas últimas palavras, “se perecer, pereci”, não são esperança, mas aceitação do desfecho.",
 it="Ester decide di presentarsi al re senza essere chiamata, pur conoscendo la legge. Le sue ultime parole, «se devo morire, morirò», non sono speranza, ma accettazione dell’esito.",
 ko="에스더는 법을 알면서도 부름 없이 왕에게 나아가기로 한다. 마지막 말 “죽으면 죽으리이다”는 희망이 아니라 결과를 받아들이겠다는 동의다."),
"job-2-10": dict(
 pt="Resposta à mulher, que sugeriu que ele amaldiçoasse a Deus e morresse. Nesse momento, Jó está sentado na cinza, raspando-se com um caco de barro.",
 it="Risposta alla moglie, che gli aveva suggerito di maledire Dio e morire. In quel momento Giobbe siede nella cenere e si gratta con un coccio.",
 ko="하나님을 욕하고 죽으라고 한 아내에게 주는 대답이다. 그때 욥은 재 가운데 앉아 기와 조각으로 몸을 긁고 있었다."),
"job-14-1": dict(
 pt="Jó fala da vida humana em geral, no meio de uma discussão sobre a sua própria. As imagens vêm da natureza: uma flor e uma sombra, ambas passageiras.",
 it="Giobbe parla della vita umana in generale, nel mezzo di una disputa sulla propria. Le immagini vengono dalla natura: un fiore e un’ombra, entrambi di breve durata.",
 ko="욥은 자기 삶을 두고 다투는 가운데 사람의 삶 일반에 대해 말한다. 비유는 자연에서 왔다. 꽃과 그림자, 둘 다 오래가지 않는다."),
"job-29-2": dict(
 pt="Jó lembra como as coisas eram antes, no único capítulo do livro dedicado inteiramente à saudade do passado. Ele não pede que volte; apenas o enumera.",
 it="Giobbe ricorda com’era prima, nell’unico capitolo del libro dedicato interamente alla nostalgia del passato. Non chiede che torni: si limita a elencarlo.",
 ko="욥이 지난날을 회상한다. 이 책에서 온통 과거에 대한 그리움으로 채워진 유일한 장이다. 그는 되돌려 달라고 하지 않고 그저 열거한다."),
"psa-5-3": dict(
 pt="Um salmo matinal de Davi. O verbo traduzido como “apresentar” vem da prática dos sacrifícios: descrevia arrumar a lenha ao amanhecer.",
 it="Un salmo mattutino di Davide. Il verbo reso con «mi presento» viene dalla pratica dei sacrifici: indicava il disporre la legna all’alba.",
 ko="다윗의 아침 시다. “기도하고”로 번역된 히브리어 동사는 제사에서 온 말로, 새벽에 장작을 벌여 놓는 일을 가리켰다."),
"psa-6-6": dict(
 pt="Davi escreve que se esgota de tanto gemer durante a noite e encharca a cama de lágrimas. O salmo é classificado como penitencial, mas sua queixa é corporal.",
 it="Davide scrive che si sfinisce a gemere per tutta la notte e bagna di lacrime il letto. Il salmo è annoverato tra i penitenziali, ma il suo lamento è fisico.",
 ko="다윗은 밤새 탄식하여 곤핍하고 눈물로 침상을 적신다고 쓴다. 참회시로 분류되지만 그 탄식은 몸의 고통에 관한 것이다."),
"psa-9-9": dict(
 pt="A palavra traduzida como “refúgio” significa uma altura que não se alcança por baixo. Este salmo e o seguinte formam juntos um único acróstico; a Bíblia grega os conta como um só.",
 it="La parola resa con «alto ricetto» indica un’altura irraggiungibile dal basso. Questo salmo e il successivo formano insieme un unico acrostico; la Bibbia greca li conta come uno solo.",
 ko="“산성”으로 번역된 말은 아래에서 닿을 수 없는 높은 곳을 뜻한다. 이 시와 다음 시는 함께 하나의 이합체 시를 이루며, 그리스어 성경은 둘을 한 편으로 센다."),
"psa-17-8": dict(
 pt="Duas imagens seguidas: a menina dos olhos, protegida sem pensar, e uma ave que abriga os filhotes debaixo da asa. Ambas vêm do reflexo, não da escolha.",
 it="Due immagini di seguito: la pupilla dell’occhio, che si protegge senza pensarci, e un uccello che ripara i piccoli sotto l’ala. Entrambe vengono dal riflesso, non dalla scelta.",
 ko="두 비유가 잇달아 나온다. 생각할 겨를 없이 보호하는 눈동자, 그리고 새끼를 날개 아래 감추는 새다. 둘 다 선택이 아니라 반사에서 온 이미지다."),
"psa-18-28": dict(
 pt="O salmo foi escrito no dia em que Davi escapou de Saul. A lâmpada aqui é a mesma pequena lamparina de barro que dá nome ao aplicativo.",
 it="Il salmo fu scritto il giorno in cui Davide scampò a Saul. La lampada di cui si parla è la stessa piccola lampada d’argilla che dà il nome all’app.",
 ko="다윗이 사울의 손에서 벗어난 날에 지은 시다. 여기 나오는 등불은 이 앱의 이름이 된 바로 그 작은 진흙 등잔이다."),
"psa-24-1": dict(
 pt="Um salmo para a entrada no templo, cantado às portas. A afirmação de que a terra inteira pertence a Deus era feita logo antes de pisar num pequeno pedaço de chão.",
 it="Un salmo per l’ingresso al tempio, cantato alle porte. L’affermazione che tutta la terra appartiene a Dio si pronunciava subito prima di mettere piede su un piccolo appezzamento.",
 ko="성전에 들어갈 때 문 앞에서 부르던 시다. 온 땅이 여호와의 것이라는 고백은 작은 땅 한 뙈기에 들어서기 직전에 불렸다."),
"psa-41-1": dict(
 pt="Salmo de um doente que escreve que as visitas vêm e mentem na cara dele. A frase sobre cuidar do pobre está no início, antes da queixa.",
 it="Il salmo di un malato che scrive che i visitatori vengono e gli mentono in faccia. La frase sulla cura del povero sta all’inizio, prima del lamento.",
 ko="병든 사람의 시로, 그는 문병 온 이들이 면전에서 거짓을 말한다고 쓴다. 빈약한 자를 돌보라는 구절은 탄식보다 앞, 첫머리에 놓여 있다."),
"psa-50-15": dict(
 pt="Um salmo em que Deus recusa os sacrifícios, explicando que não tem fome. Em vez de carne, pede ação de graças e que o invoquem na angústia.",
 it="Un salmo in cui Dio rifiuta i sacrifici, spiegando di non avere fame. Al posto della carne chiede gratitudine e di essere invocato nel momento del bisogno.",
 ko="하나님이 배고프지 않다며 제물을 사양하는 시다. 고기 대신 감사와, 환난 날에 부르는 것을 청한다."),
"psa-57-1": dict(
 pt="O título situa este salmo quando Davi se escondia de Saul numa caverna. A sombra das asas é uma imagem de ave, não de arquitetura.",
 it="L’intestazione colloca questo salmo nel periodo in cui Davide si nascondeva da Saul in una grotta. L’ombra delle ali è un’immagine presa dagli uccelli, non dall’architettura.",
 ko="표제는 이 시를 다윗이 사울을 피해 굴에 숨어 있던 때로 둔다. 날개 그늘은 건축물이 아니라 새의 이미지다."),
"psa-70-5": dict(
 pt="Um salmo curto, feito inteiramente de um pedido de pressa. As últimas palavras no hebraico são “não te detenhas”, e ali ele se interrompe.",
 it="Un salmo breve, fatto interamente di una richiesta di affrettarsi. Le ultime parole del testo ebraico sono «non tardare», e lì si interrompe.",
 ko="서둘러 달라는 간구로만 이루어진 짧은 시다. 히브리어 본문의 마지막 말은 “지체하지 마소서”이고, 시는 거기서 끊긴다."),
"psa-78-4": dict(
 pt="O início do salmo histórico mais longo. Depois ele reconta com honestidade também os fracassos do povo: a tarefa é transmitir, não melhorar o que aconteceu.",
 it="L’inizio del più lungo salmo storico. In seguito racconta con onestà anche i fallimenti del popolo: il compito è tramandare, non abbellire.",
 ko="가장 긴 역사 시의 첫머리다. 이어서 백성의 실패도 정직하게 되짚는다. 할 일은 미화가 아니라 전하는 것이다."),
"psa-82-3": dict(
 pt="Um salmo que acusa os juízes de julgar injustamente e favorecer os poderosos. A exigência é dirigida a quem tem o poder de decidir.",
 it="Un salmo che accusa i giudici di giudicare ingiustamente e di favorire i potenti. La richiesta è rivolta a chi ha il potere di decidere.",
 ko="재판장들이 불공평하게 판단하고 강자를 편든다고 고발하는 시다. 이 요구는 판결할 권세를 가진 자들을 향한다."),
"psa-84-5": dict(
 pt="Um salmo de peregrino. O hebraico fala de pessoas que têm os caminhos no coração: atravessam um vale de lágrimas e o transformam em fonte.",
 it="Un salmo del pellegrino. L’ebraico parla di persone che hanno le strade nel cuore: attraversano una valle di pianto e la trasformano in una sorgente.",
 ko="순례자의 시다. 히브리어 본문은 마음에 큰길이 있는 사람들을 말한다. 그들은 눈물 골짜기를 지나며 그곳을 샘으로 바꾼다."),
"psa-92-14": dict(
 pt="Um salmo para o sábado. Imagem botânica: tamareiras e cedros dão mais quanto mais velhos ficam, e todo ouvinte sabia disso.",
 it="Un salmo per il sabato. Un’immagine botanica: le palme da dattero e i cedri fruttificano tanto più quanto più invecchiano, e ogni ascoltatore lo sapeva.",
 ko="안식일의 찬송 시다. 식물에서 온 이미지로, 종려나무와 백향목은 늙을수록 더 많은 열매를 맺으며 듣는 이는 모두 그것을 알았다."),
"psa-115-1": dict(
 pt="Um salmo do ciclo da Páscoa que começa recusando o mérito. Depois zomba dos ídolos que têm olhos e ouvidos que não funcionam.",
 it="Un salmo del ciclo pasquale che si apre rifiutando il merito. Poi deride gli idoli che hanno occhi e orecchie che non funzionano.",
 ko="유월절에 부르던 시편 묶음에 속하며, 영광을 사양하는 말로 시작한다. 이어서 눈과 귀가 있어도 쓰지 못하는 우상을 조롱한다."),
"psa-117-1": dict(
 pt="O salmo mais curto do Saltério, com duas linhas. Mesmo assim, ele se dirige a todas as nações, e não a Israel, o que é raro no Saltério.",
 it="Il salmo più breve del Salterio, lungo due righe. Eppure si rivolge a tutti i popoli e non a Israele, cosa rara nel Salterio.",
 ko="시편에서 가장 짧은 시로, 두 줄이다. 그런데도 이스라엘이 아닌 모든 나라를 향하는데, 이는 시편에서 드문 일이다."),
"psa-119-130": dict(
 pt="Do salmo mais longo, um acróstico sobre a lei. O verbo traduzido como “revelação” significa literalmente abertura, como quando se abre uma porta e a luz entra.",
 it="Dal salmo più lungo, un acrostico sulla legge. Il termine reso con «rivelazione» significa letteralmente apertura: come quando si apre una porta ed entra la luce.",
 ko="율법에 관한 이합체 시이자 가장 긴 시편에서 나온다. “열므로”로 번역된 말은 문을 열어 빛이 들어오듯 여는 것을 뜻한다."),
"psa-150-6": dict(
 pt="A última frase de todo o Saltério, depois de cento e quarenta e nove salmos que incluíam maldições e queixas sobre o silêncio de Deus.",
 it="L’ultima riga dell’intero Salterio, dopo centoquarantanove salmi tra cui c’erano anche maledizioni e lamenti sul silenzio di Dio.",
 ko="시편 전체의 마지막 구절이다. 앞의 백마흔아홉 편에는 저주도, 하나님의 침묵에 대한 탄식도 있었다."),
"pro-6-6": dict(
 pt="O conselho de olhar para a formiga é dado a um preguiçoso. O argumento se apoia no fato de a formiga não ter chefe nem supervisor, e o trabalho ser feito mesmo assim.",
 it="Il consiglio di guardare la formica è dato a un pigro. L’argomento si basa sul fatto che la formica non ha né capo né sorvegliante, eppure il lavoro si fa.",
 ko="개미를 보라는 조언은 게으른 자에게 주어진다. 개미에게는 두령도 감독자도 없는데 일이 된다는 것이 논거다."),
"pro-13-12": dict(
 pt="Um provérbio sobre o que a espera adiada faz fisicamente com uma pessoa. As duas imagens são corporais: um coração doente e uma árvore da vida.",
 it="Un detto su ciò che l’attesa prolungata fa fisicamente a una persona. Entrambe le immagini sono corporee: un cuore malato e un albero di vita.",
 ko="미뤄진 기다림이 사람의 몸에 어떤 일을 하는지에 관한 잠언이다. 두 이미지 모두 몸에 관한 것이다. 상한 마음과 생명나무다."),
"pro-17-17": dict(
 pt="O provérbio distingue o amigo do irmão: o primeiro ama em todo tempo, o segundo é justamente para a hora da angústia. Não são sinônimos, mas dois casos diferentes.",
 it="Il detto distingue l’amico dal fratello: il primo ama sempre, il secondo serve proprio nella sventura. Non sono sinonimi, ma due casi diversi.",
 ko="이 잠언은 친구와 형제를 구별한다. 친구는 언제나 사랑하고, 형제는 바로 위급할 때를 위해 있다. 동의어가 아니라 서로 다른 두 경우다."),
"pro-25-11": dict(
 pt="De uma coleção reunida pelos homens do rei Ezequias. Imagem de joalheiro: frutas de ouro em engaste de prata, algo caro e feito exatamente sob medida.",
 it="Da una raccolta compilata dagli uomini del re Ezechia. Un’immagine da gioielliere: frutti d’oro in una montatura d’argento, un oggetto prezioso fatto esattamente su misura.",
 ko="히스기야 왕의 신하들이 엮은 모음집에 있다. 은 쟁반에 놓인 금 사과, 곧 비싸고 꼭 맞게 만든 세공품의 이미지다."),
"pro-28-13": dict(
 pt="Um provérbio sobre duas maneiras de lidar com a culpa: encobri-la ou nomeá-la. O verbo “encobre” é o mesmo que Gênesis usa para Adão se escondendo.",
 it="Un detto su due modi di affrontare la colpa: nasconderla o nominarla. Il verbo per «nasconde» è lo stesso che la Genesi usa per Adamo che si nasconde.",
 ko="죄를 다루는 두 길, 숨기느냐 밝히느냐에 관한 잠언이다. “숨기는”이라는 동사는 창세기에서 아담이 숨은 일을 묘사한 말과 같다."),
"pro-30-8": dict(
 pt="Uma oração rara num livro de provérbios. O autor não pede pobreza nem riqueza e explica os dois riscos: esquecer quando está farto, roubar quando passa necessidade.",
 it="Una preghiera rara in un libro di detti. L’autore non chiede né povertà né ricchezza e spiega entrambi i rischi: dimenticare quando si è sazi, rubare quando si è nel bisogno.",
 ko="잠언에서 보기 드문 기도다. 저자는 가난도 부도 구하지 않으며 두 위험을 설명한다. 배부르면 잊고, 궁핍하면 도둑질한다는 것이다."),
"ecc-7-3": dict(
 pt="O autor aconselha ir a uma casa de luto, e não a uma casa de banquete. O motivo é prático: ali se vê como tudo termina para todos.",
 it="L’autore consiglia di andare in una casa in lutto piuttosto che in una casa in festa. La sua ragione è pratica: lì si vede come finisce per tutti.",
 ko="저자는 잔칫집보다 초상집에 가라고 권한다. 이유는 실용적이다. 거기서는 모든 사람의 끝이 어떠한지 보인다."),
"sng-2-11": dict(
 pt="Um convite para sair depois do inverno, num livro sobre dois amantes. Naquela terra as chuvas vinham no inverno, e o fim delas encerrava o tempo dentro de casa.",
 it="Un invito a uscire dopo l’inverno, in un libro su due innamorati. In quella terra le piogge cadevano d’inverno, e con la loro fine finiva anche lo stare chiusi in casa.",
 ko="두 연인에 관한 책에서 겨울이 지났으니 나오라고 부르는 말이다. 그 땅에서는 겨울에 비가 내렸고, 비가 그치면 집 안에 머물던 시간도 끝났다."),
"isa-45-3": dict(
 pt="Dito sobre Ciro, um rei persa que não conhecia o Deus de Israel. A promessa de tesouros nas trevas é feita a um estrangeiro, não a alguém do próprio povo.",
 it="Detto di Ciro, un re persiano che non conosceva il Dio d’Israele. La promessa di tesori nelle tenebre è fatta a un estraneo, non a uno dei loro.",
 ko="이스라엘의 하나님을 알지 못한 바사 왕 고레스에 관한 말이다. 흑암 중의 보화를 주겠다는 약속은 자기 백성이 아니라 바깥사람에게 주어진다."),
"isa-60-1": dict(
 pt="Dirigido a uma cidade em ruínas. A ordem de se levantar e resplandecer é dada a quem não tem luz própria; a fonte é nomeada na linha seguinte.",
 it="Rivolto a una città in rovina. L’ordine di alzarsi e risplendere è dato a chi non ha luce propria; la fonte è nominata nella riga successiva.",
 ko="폐허로 누운 성을 향한 말이다. 일어나 빛을 발하라는 명령은 스스로는 빛이 없는 이에게 주어지며, 그 빛의 근원은 다음 줄에 나온다."),
"isa-64-8": dict(
 pt="Uma frase de uma oração coletiva de arrependimento, em que o povo admite que todos murcharam como folha. A imagem do barro ressalta dependência, não humildade.",
 it="Una frase da una preghiera collettiva di pentimento, in cui il popolo ammette che tutti sono avvizziti come foglie. L’immagine dell’argilla sottolinea la dipendenza, non l’umiltà.",
 ko="백성이 모두 잎사귀같이 시들었다고 고백하는 공동 회개 기도의 한 줄이다. 진흙의 이미지는 겸손보다 의존을 강조한다."),
"isa-66-13": dict(
 pt="O último capítulo do livro. Uma comparação materna é rara nos profetas, e ela vem justamente no fim, depois de sessenta e cinco capítulos em outro registro.",
 it="L’ultimo capitolo del libro. Un paragone materno è raro nei profeti, e arriva proprio alla fine, dopo sessantacinque capitoli di tutt’altro tono.",
 ko="책의 마지막 장이다. 어머니에 빗댄 비유는 선지서에서 드문데, 다른 어조의 예순다섯 장을 지난 맨 끝에 나온다."),
"jer-2-13": dict(
 pt="O profeta nomeia dois males seguidos, e o segundo são cisternas que não retêm água. Num país sem rios, esse era o erro mais caro e mais frustrante.",
 it="Il profeta nomina due mali di seguito, e il secondo sono cisterne che non trattengono l’acqua. In un paese senza fiumi era l’errore più costoso e più amaro.",
 ko="선지자는 두 가지 악을 잇달아 꼽는데, 둘째는 물을 담지 못하는 웅덩이다. 강이 없는 나라에서 이는 가장 값비싸고 가장 분한 실수였다."),
"jer-8-22": dict(
 pt="O bálsamo de Gileade era um remédio conhecido, transportado pelas caravanas. A pergunta é retórica e amarga: o remédio existe, a cura não.",
 it="Il balsamo di Galaad era una medicina famosa, trasportata dalle carovane. La domanda è retorica e amara: la medicina c’è, la guarigione no.",
 ko="길르앗 유향은 대상들이 실어 나르던 이름난 약이었다. 질문은 반어적이고 쓰라리다. 약은 있는데 낫지 않는다."),
"jer-18-6": dict(
 pt="Jeremias é enviado a uma oficina para ver alguém trabalhar. O vaso saiu errado nas mãos do oleiro, e ele fez outro com o mesmo barro: essa é toda a lição.",
 it="Geremia viene mandato in una bottega a guardare qualcuno lavorare. Il vaso non riuscì nelle mani del vasaio, che ne fece un altro con la stessa argilla: tutta qui la lezione.",
 ko="예레미야는 토기장이의 집에 가서 일하는 것을 보라는 명을 받는다. 그릇이 손에서 터지자 토기장이는 같은 진흙으로 다른 그릇을 만들었다. 교훈은 그것이 전부다."),
"jer-20-9": dict(
 pt="Jeremias acaba de passar uma noite no tronco e de declarar que não profetizará mais. Esta é a sua confissão de por que ficar calado não funcionou.",
 it="Geremia ha appena passato una notte ai ceppi e ha dichiarato che non profetizzerà più. Questa è la sua ammissione del perché tacere non ha funzionato.",
 ko="예레미야는 막 차꼬에 채워진 채 하룻밤을 보내고 다시는 예언하지 않겠다고 했다. 이 구절은 왜 잠잠할 수 없었는지에 대한 고백이다."),
"jer-31-25": dict(
 pt="Depois desta frase, o profeta acrescenta que despertou e que seu sono lhe tinha sido doce. É o único lugar do livro em que ele menciona o próprio sono.",
 it="Dopo questa frase il profeta aggiunge che si svegliò e che il suo sonno era stato dolce. È l’unico punto del libro in cui parla del proprio sonno.",
 ko="이 구절 뒤에 선지자는 깨어 보니 잠이 달았다고 덧붙인다. 책에서 그가 자기 잠을 언급하는 유일한 곳이다."),
"lam-3-31": dict(
 pt="Do lamento pela Jerusalém destruída. Diz que Deus não aflige as pessoas “de coração”, isto é, não de bom grado.",
 it="Dal lamento su Gerusalemme distrutta. Si dice che Dio non affligge le persone per desiderio del cuore, cioè non lo fa volentieri.",
 ko="무너진 예루살렘을 두고 부른 애가에 나온다. 주께서 사람을 근심하게 하심은 본심이 아니라고, 곧 원해서가 아니라고 말한다."),
"ezk-22-30": dict(
 pt="Deus diz que procurou alguém que se colocasse na brecha do muro e não encontrou ninguém. A frase termina com a busca fracassada.",
 it="Dio dice di aver cercato qualcuno che si mettesse sulla breccia del muro e di non aver trovato nessuno. La frase si chiude con la ricerca fallita.",
 ko="하나님은 성 무너진 데를 막아설 사람을 찾았으나 찾지 못했다고 말한다. 구절은 그 찾음이 실패했다는 말로 끝난다."),
"dan-2-22": dict(
 pt="Daniel diz isso à noite, depois de lhe ser revelado o sonho do rei. A execução de todos os sábios da Babilônia já tinha sido ordenada, inclusive a dele.",
 it="Daniele lo dice di notte, dopo che gli è stato rivelato il sogno del re. L’esecuzione di tutti i saggi di Babilonia era già stata ordinata, lui compreso.",
 ko="다니엘이 밤에 왕의 꿈을 계시받은 뒤 한 말이다. 바벨론의 모든 박사를 죽이라는 명령이 이미 내려졌고, 거기에는 그 자신도 포함되어 있었다."),
"hos-6-6": dict(
 pt="Jesus cita esta frase duas vezes, em discussões sobre com quem se pode comer e o que se pode fazer no sábado. Em Oseias, ela é dita sobre o culto formal.",
 it="Gesù cita questa frase due volte nelle dispute su con chi si può mangiare e su che cosa si può fare di sabato. In Osea è detta a proposito del culto formale.",
 ko="예수는 누구와 함께 먹을 수 있는지, 안식일에 무엇을 할 수 있는지를 두고 논쟁할 때 이 구절을 두 번 인용한다. 호세아서에서는 형식적인 예배에 관해 한 말이다."),
"jol-2-28": dict(
 pt="A profecia enumera quem normalmente não recebia palavra: filhos e filhas, velhos, jovens, servos e servas. A própria lista é a notícia.",
 it="La profezia elenca chi di solito non riceveva la parola: figli e figlie, anziani, giovani, schiavi e schiave. L’elenco stesso è la novità.",
 ko="이 예언은 보통 말씀을 받지 못하던 이들을 꼽는다. 자녀들, 늙은이, 젊은이, 남종과 여종이다. 그 명단 자체가 소식이다."),
"jon-4-2": dict(
 pt="Jonas explica por que fugiu: sabia desde o início que a cidade seria poupada. É justamente a misericórdia que o deixa irado, nada mais.",
 it="Giona spiega perché era fuggito: sapeva fin dall’inizio che la città sarebbe stata risparmiata. È proprio la misericordia a farlo arrabbiare, nient’altro.",
 ko="요나는 자기가 달아난 이유를 설명한다. 처음부터 그 성이 용서받을 줄 알았다는 것이다. 그가 화내는 것은 다른 무엇이 아니라 바로 그 자비다."),
"mic-4-4": dict(
 pt="A imagem da paz não é um palácio, mas a própria videira e a própria figueira, sem ninguém para causar medo. A medida de bem-estar do profeta é inteiramente doméstica.",
 it="L’immagine della pace non è un palazzo, ma la propria vite e il proprio fico, senza nessuno che spaventi. La misura del benessere, per il profeta, è del tutto domestica.",
 ko="평화의 그림은 궁전이 아니라, 두렵게 할 자 없이 자기 포도나무와 무화과나무 아래 앉은 모습이다. 선지자가 말하는 평안의 기준은 철저히 일상적이다."),
"hag-2-4": dict(
 pt="Dito aos construtores do segundo templo, que ouvem dos mais velhos que o primeiro era incomparavelmente melhor. A instrução é simples: sejam fortes e trabalhem.",
 it="Detto ai costruttori del secondo tempio, a cui gli anziani dicono che il primo era incomparabilmente migliore. L’ordine è semplice: siate forti e lavorate.",
 ko="첫 성전이 비할 수 없이 더 좋았다는 노인들의 말을 듣는 둘째 성전 건축자들에게 한 말이다. 명령은 단순하다. 굳세게 하여 일하라는 것이다."),
"zec-9-12": dict(
 pt="A expressão “prisioneiros da esperança” é um paradoxo deliberado: o povo continua cativo, e a esperança é apontada como o que o sustenta, não como o que o libertou.",
 it="L’espressione «prigionieri della speranza» è un paradosso voluto: il popolo è ancora in cattività, e la speranza è indicata come ciò che lo trattiene, non come ciò che l’ha liberato.",
 ko="“소망을 품은 갇힌 자들아”라는 부름은 의도된 역설이다. 백성은 여전히 사로잡혀 있고, 소망은 그들을 풀어 준 것이 아니라 붙들고 있는 것으로 불린다."),
"mat-5-44": dict(
 pt="Do Sermão do Monte. Os ouvintes viviam sob ocupação romana, então “inimigo” significava para eles pessoas armadas concretas, não uma abstração.",
 it="Dal Discorso della montagna. Gli ascoltatori vivevano sotto l’occupazione romana, e per loro «nemico» indicava persone armate ben precise, non un’astrazione.",
 ko="산상수훈에 나온다. 듣는 이들은 로마의 점령 아래 살았기에 “원수”는 추상이 아니라 무기를 든 구체적인 사람들이었다."),
"mat-11-29": dict(
 pt="Dito na Galileia a quem já não tem forças. O jugo era colocado numa parelha: o animal jovem aprendia andando ao lado de um adulto, não sozinho.",
 it="Detto in Galilea a chi non ce la fa più. Il giogo si metteva a una coppia di animali: il giovane imparava camminando accanto a uno adulto, non da solo.",
 ko="갈릴리에서 더 버틸 힘이 없는 사람들에게 한 말이다. 멍에는 두 마리에게 함께 메웠고, 어린 짐승은 혼자가 아니라 다 자란 짐승 곁에서 걸으며 배웠다."),
"mat-18-21": dict(
 pt="Pedro propõe perdoar sete vezes, achando-se generoso: os rabinos da época falavam em três. A resposta leva a conta a um ponto em que contar não faz sentido.",
 it="Pietro propone di perdonare sette volte, credendosi generoso: i rabbini dell’epoca parlavano di tre. La risposta porta il conto dove contare non ha più senso.",
 ko="베드로는 일곱 번 용서하자며 그것이 너그럽다고 생각한다. 당시 랍비들은 세 번을 말했다. 대답은 횟수를 세는 것이 무의미한 영역으로 옮겨 놓는다."),
"mat-23-37": dict(
 pt="Dito sobre a cidade no fim de um discurso de repreensão. A imagem da galinha com os pintinhos quebra o tom de repente, e a fala termina com as palavras “vós não o quisestes”.",
 it="Detto sulla città alla fine di un discorso di rimprovero. L’immagine della chioccia con i pulcini spezza il tono di colpo e si chiude con le parole «voi non avete voluto».",
 ko="꾸짖는 설교 끝에 그 성을 두고 한 말이다. 병아리를 품는 암탉의 이미지가 어조를 갑자기 바꾸고, “너희가 원치 아니하였도다”로 끝난다."),
"mat-26-41": dict(
 pt="Dito aos discípulos que dormiram no jardim enquanto ele orava. Lucas acrescenta que dormiam de tristeza, não por descuido.",
 it="Detto ai discepoli che si erano addormentati nel giardino mentre lui pregava. Luca aggiunge che dormivano per la tristezza, non per noncuranza.",
 ko="예수가 기도하는 동안 동산에서 잠든 제자들에게 한 말이다. 누가는 그들이 방심해서가 아니라 슬픔 때문에 잠들었다고 덧붙인다."),
"mrk-2-17": dict(
 pt="Resposta a escribas indignados por ele comer com cobradores de impostos. O argumento é médico, e foi dito à mesa de um deles.",
 it="Risposta agli scribi indignati perché mangiava con gli esattori delle tasse. L’argomento è medico, e fu pronunciato proprio alla tavola di uno di loro.",
 ko="그가 세리들과 함께 먹는 것에 분개한 서기관들에게 주는 대답이다. 논거는 의학적이고, 바로 그 세리 가운데 한 사람의 식탁에서 한 말이다."),
"mrk-9-23": dict(
 pt="Resposta ao pai que disse “se tu podes”. Jesus devolve o “se” a ele, e a frase seguinte do pai se torna a resposta mais honesta dos Evangelhos.",
 it="Risposta al padre che aveva detto «se puoi». Gesù gli restituisce quel «se», e la frase successiva del padre diventa la risposta più onesta dei Vangeli.",
 ko="“할 수 있거든”이라고 말한 아버지에게 주는 대답이다. 예수는 그 “할 수 있거든”을 되돌려 주고, 아버지의 다음 말은 복음서에서 가장 정직한 대답이 된다."),
"mrk-14-8": dict(
 pt="Dito sobre uma mulher que derramou um perfume caro sobre a cabeça dele. Os presentes se indignaram com o desperdício; ele não mediu a quantidade, mas o momento.",
 it="Detto di una donna che gli aveva versato sul capo un profumo costoso. I presenti si indignarono per lo spreco; lui valutò non la quantità, ma il momento.",
 ko="값비싼 향유를 그의 머리에 부은 여자에 관한 말이다. 곁에 있던 이들은 허비라며 분개했지만, 그는 양이 아니라 때를 보았다."),
"luk-2-19": dict(
 pt="Dito sobre Maria na noite em que os pastores chegaram com o relato dos anjos. Todos os outros se admiravam em voz alta; ela ficou calada e guardou tudo.",
 it="Detto di Maria nella notte in cui arrivarono i pastori con il loro racconto sugli angeli. Tutti si stupivano ad alta voce; lei taceva e custodiva tutto nella memoria.",
 ko="목자들이 천사 이야기를 들고 찾아온 밤의 마리아에 관한 말이다. 모두가 소리 내어 놀랐지만, 그는 말없이 그것을 마음에 간직했다."),
"luk-22-32": dict(
 pt="Dito a Pedro antes da negação, não depois. Jesus não promete que ele não vai cair; diz que orou pela fé dele e lhe dá uma tarefa para depois.",
 it="Detto a Pietro prima del rinnegamento, non dopo. Gesù non promette che non cadrà: dice di aver pregato per la sua fede e gli affida in anticipo un compito per dopo.",
 ko="부인한 뒤가 아니라 그 전에 베드로에게 한 말이다. 예수는 그가 넘어지지 않으리라 약속하지 않고, 그의 믿음을 위해 기도했다며 그 뒤에 할 일을 미리 맡긴다."),
"luk-22-61": dict(
 pt="Pedro o nega pela terceira vez, um galo canta, e Jesus, conduzido pelo pátio, se volta e olha para ele. Nenhuma palavra é trocada.",
 it="Pietro lo rinnega per la terza volta, un gallo canta, e Gesù, condotto attraverso il cortile, si volta e lo guarda. In quel momento non ci sono parole.",
 ko="베드로가 세 번째로 부인하자 닭이 울고, 뜰을 지나 끌려가던 예수가 돌이켜 그를 본다. 그 순간 오간 말은 없다."),
"jhn-2-5": dict(
 pt="As últimas palavras de Maria nos Evangelhos, ditas aos serventes numa festa de casamento em que o vinho acabou. Ela não diz mais nada no Evangelho de João.",
 it="Le ultime parole di Maria nei Vangeli, rivolte ai servi a una festa di nozze in cui era finito il vino. Nel Vangelo di Giovanni non dice nient’altro.",
 ko="복음서에 기록된 마리아의 마지막 말로, 포도주가 떨어진 혼인 잔치에서 하인들에게 한 말이다. 요한복음에서 그는 이후 아무 말도 하지 않는다."),
"jhn-5-6": dict(
 pt="A pergunta é feita a um homem que estava deitado junto ao tanque havia trinta e oito anos. Ele não responde que sim; explica por que nunca dá certo.",
 it="La domanda è rivolta a un uomo che giaceva presso la piscina da trentotto anni. Non risponde di sì: spiega perché non ci riesce mai.",
 ko="못가에 삼십팔 년 동안 누워 있던 사람에게 던진 질문이다. 그는 “예”라고 답하지 않고, 왜 늘 안 되는지를 설명한다."),
"jhn-13-7": dict(
 pt="Resposta a Pedro, que se recusava a deixar que lhe lavassem os pés. A promessa de compreensão é colocada no futuro, não dada na hora.",
 it="Risposta a Pietro, che rifiutava di farsi lavare i piedi. La promessa di capire è collocata nel futuro, non data subito.",
 ko="발 씻기기를 거절한 베드로에게 주는 대답이다. 깨달음은 그 자리에서 주어지지 않고 나중으로 미뤄진다."),
"jhn-14-18": dict(
 pt="A palavra traduzida como “órfãos” significa literalmente privados de um dos pais. Dito aos discípulos horas antes de o perderem.",
 it="La parola resa con «orfani» significa letteralmente privati di un genitore. Detto ai discepoli poche ore prima di perderlo.",
 ko="“고아”로 번역된 말은 문자 그대로 부모를 잃은 자를 뜻한다. 그를 잃기 몇 시간 전인 제자들에게 한 말이다."),
"jhn-19-30": dict(
 pt="A última palavra da cruz no Evangelho de João, uma única palavra em grego. Era usada em recibos para indicar uma dívida totalmente paga.",
 it="L’ultima parola dalla croce nel Vangelo di Giovanni, una sola parola in greco. Si usava sulle ricevute per indicare un debito pagato per intero.",
 ko="요한복음에서 십자가 위의 마지막 말로, 헬라어로는 한 단어다. 이 말은 영수증에 빚을 다 갚았다고 표시할 때 쓰였다."),
"jhn-20-15": dict(
 pt="Maria chora junto ao túmulo vazio e o confunde com o jardineiro. Ela o reconhece não pela vista, mas quando ele diz o nome dela.",
 it="Maria piange presso il sepolcro vuoto e lo scambia per il giardiniere. Lo riconosce non dall’aspetto, ma quando lui la chiama per nome.",
 ko="마리아는 빈 무덤 앞에서 울다가 그를 동산지기로 여긴다. 모습을 보고서가 아니라, 그가 자기 이름을 부를 때에야 그를 알아본다."),
"act-3-6": dict(
 pt="Pedro responde a um mendigo à porta do templo que lhe tinha pedido dinheiro. Começa admitindo que não tem nenhum e só então oferece outra coisa.",
 it="Pietro risponde a un mendicante alla porta del tempio che chiedeva l’elemosina. Comincia ammettendo di non avere denaro, e solo dopo offre qualcos’altro.",
 ko="베드로가 성전 문 앞에서 돈을 구하던 걸인에게 대답한다. 그는 돈이 없다는 고백으로 시작하고, 그다음에야 다른 것을 내민다."),
"act-14-22": dict(
 pt="Paulo diz isso depois de voltar a uma cidade onde pouco antes tinha sido apedrejado e arrastado para fora dos muros, dado como morto.",
 it="Paolo lo dice dopo essere tornato in una città dove poco prima era stato lapidato e trascinato fuori dalle mura, creduto morto.",
 ko="바울이 얼마 전 돌에 맞아 죽은 줄 알고 성 밖으로 끌려 나갔던 그 성에 다시 돌아가 한 말이다."),
"act-28-15": dict(
 pt="Paulo está sendo levado a Roma sob guarda, e cristãos de Roma caminham muitos quilômetros para encontrá-lo. Lucas registra que, ao vê-los, Paulo cobrou ânimo.",
 it="Paolo viene condotto a Roma sotto scorta, e i cristiani di Roma percorrono molte miglia per andargli incontro. Luca annota che, vedendoli, Paolo prese coraggio.",
 ko="바울이 호송되어 로마로 갈 때, 로마의 그리스도인들이 먼 길을 나와 그를 맞는다. 누가는 바울이 그들을 보고 담대한 마음을 얻었다고 적는다."),
"rom-5-3": dict(
 pt="Uma corrente de quatro elos, com a tribulação em primeiro lugar. Paulo não diz que a tribulação é boa; descreve o que cresce dela quando é suportada.",
 it="Una catena di quattro anelli, con la tribolazione al primo posto. Paolo non dice che la tribolazione sia buona: descrive ciò che ne nasce quando la si sopporta.",
 ko="환난이 맨 앞에 놓인 네 고리의 사슬이다. 바울은 환난이 좋다고 말하지 않고, 견딜 때 그로부터 무엇이 자라나는지 묘사한다."),
"rom-12-1": dict(
 pt="Uma expressão deliberadamente contraditória: um sacrifício é, por definição, algo morto, e aqui é chamado de vivo. É assim que começa a metade prática da carta.",
 it="Un’espressione volutamente contraddittoria: un sacrificio è per definizione morto, e qui è detto vivente. Così comincia la metà pratica della lettera.",
 ko="일부러 모순되게 쓴 표현이다. 제물은 본디 죽은 것인데 여기서는 산 제사라 불린다. 편지의 실천적인 후반부가 이렇게 시작된다."),
"1co-3-6": dict(
 pt="Paulo trata de uma divisão numa comunidade em que uns se diziam seus seguidores e outros, de Apolo. Ele divide o trabalho em etapas para tirar o motivo da disputa.",
 it="Paolo affronta una divisione in una comunità in cui alcuni si dicevano suoi seguaci e altri di Apollo. Divide il lavoro in fasi per togliere il motivo della disputa.",
 ko="바울은 어떤 이는 바울에게, 어떤 이는 아볼로에게 속했다고 하는 공동체의 분열을 다룬다. 그는 일을 단계로 나누어 다툼의 근거를 없앤다."),
"1co-12-26": dict(
 pt="Da comparação da comunidade com um corpo. O argumento é fisiológico: a dor num lugar é sentida pelo organismo inteiro, e a boa vontade não tem nada a ver com isso.",
 it="Dal paragone tra la comunità e un corpo. L’argomento è fisiologico: il dolore in un punto lo sente tutto l’organismo, e la buona volontà non c’entra.",
 ko="공동체를 몸에 빗댄 비유에서 나온다. 논거는 생리적이다. 한 곳의 아픔을 온몸이 느끼며, 이는 선의의 문제가 아니다."),
"1co-13-12": dict(
 pt="Os espelhos daquela época eram de bronze polido e davam um reflexo embaçado. A imagem fala da qualidade da visão, não da distância.",
 it="Gli specchi di allora erano di bronzo levigato e davano un riflesso offuscato. L’immagine riguarda la qualità della vista, non la distanza.",
 ko="당시 거울은 광을 낸 청동이었고 비치는 모습이 흐릿했다. 이 비유는 거리가 아니라 보이는 것의 선명도에 관한 것이다."),
"1co-15-10": dict(
 pt="Paulo acaba de se chamar o menor dos apóstolos e indigno desse nome, por ter perseguido a igreja. A frase sobre a graça responde à sua própria acusação.",
 it="Paolo si è appena definito il più piccolo degli apostoli e indegno di quel nome, perché ha perseguitato la Chiesa. La frase sulla grazia risponde alla sua stessa accusa.",
 ko="바울은 교회를 핍박했으니 사도 중 가장 작은 자요 사도라 불릴 자격도 없다고 막 말했다. 은혜에 관한 구절은 스스로에 대한 고발에 답한다."),
"2co-4-7": dict(
 pt="Os vasos de barro eram os recipientes mais baratos, e ninguém lamentava quando quebravam. O contraste entre o conteúdo e a embalagem é todo o sentido.",
 it="I vasi di argilla erano i recipienti più economici, che non dispiaceva rompere. Il contrasto tra contenuto e involucro è tutto il senso.",
 ko="질그릇은 가장 값싼 그릇이라 깨져도 아깝지 않았다. 내용물과 겉포장의 대비가 이 구절의 요점 전부다."),
"2co-5-7": dict(
 pt="Uma frase curta dentro de um raciocínio de que o visível é passageiro. O contraste não é entre fé e razão, mas entre fé e vista.",
 it="Una frase breve dentro un ragionamento sul fatto che ciò che si vede è temporaneo. Il contrasto non è tra fede e ragione, ma tra fede e visione.",
 ko="보이는 것은 잠깐이라는 논증 속의 짧은 구절이다. 대비되는 것은 믿음과 이성이 아니라 믿음과 보는 것이다."),
"2co-7-6": dict(
 pt="Paulo escreve que na Macedônia não teve descanso e foi atribulado de todos os lados. O consolo não veio por uma revelação, mas pela chegada de uma pessoa: Tito.",
 it="Paolo scrive che in Macedonia non aveva avuto pace ed era oppresso da ogni parte. La consolazione non arrivò con una rivelazione, ma con l’arrivo di una persona: Tito.",
 ko="바울은 마게도냐에서 편치 못하고 사방으로 환난을 당했다고 쓴다. 위로는 계시가 아니라 한 사람의 도착, 곧 디도를 통해 왔다."),
"gal-6-7": dict(
 pt="Uma imagem agrícola, totalmente cotidiana: o que se semeia é o que cresce, independentemente das intenções. Dito no fim de uma carta dura.",
 it="Un’immagine agricola, del tutto quotidiana: ciò che si semina è ciò che cresce, a prescindere dalle intenzioni. Detto alla fine di una lettera dura.",
 ko="아주 일상적인 농사의 이미지다. 의도와 상관없이 심은 것이 자란다. 날카로운 편지의 끝에서 한 말이다."),
"eph-2-10": dict(
 pt="A palavra traduzida como “feitura” é a raiz grega de “poema”. A frase vem logo depois da afirmação de que a salvação não vem das obras.",
 it="La parola resa con «opera» è in greco la radice di «poema». La frase segue subito l’affermazione che la salvezza non dipende dalle opere.",
 ko="“만드신 바”로 번역된 헬라어는 “시(poem)”라는 말이 나온 바로 그 단어다. 구원이 행위에서 난 것이 아니라는 말 바로 뒤에 나온다."),
"php-2-14": dict(
 pt="A instrução vem logo depois do hino sobre Cristo, que esvaziou a si mesmo. A exigência de não murmurar aparece como a conclusão tirada desse hino.",
 it="L’indicazione viene subito dopo l’inno su Cristo che svuotò sé stesso. La richiesta di non mormorare è posta come la conclusione tratta da quell’inno.",
 ko="그리스도가 자기를 비운 일을 노래한 찬가 바로 뒤에 나오는 지시다. 원망하지 말라는 요구는 그 찬가에서 끌어낸 결론으로 놓여 있다."),
"col-3-12": dict(
 pt="O verbo “revesti-vos” fala de roupas vestidas de propósito a cada manhã. Logo antes, o velho homem é descrito como algo que se tira, como um manto.",
 it="Il verbo «rivestitevi» riguarda abiti che si indossano di proposito ogni mattina. Poco prima, l’uomo vecchio è descritto come qualcosa che si toglie come una veste.",
 ko="“옷 입고”라는 동사는 매일 아침 의식적으로 입는 옷에 관한 말이다. 그 앞에서는 옛 사람을 옷처럼 벗어 버린다고 말한다."),
"1th-5-14": dict(
 pt="Três grupos e três abordagens diferentes: admoestar os ociosos, consolar os desanimados, amparar os fracos. Paulo distingue quem precisa de quê.",
 it="Tre gruppi e tre approcci diversi: ammonire gli indisciplinati, confortare gli scoraggiati, sostenere i deboli. Paolo distingue di che cosa ha bisogno ciascuno.",
 ko="세 부류에 세 가지 다른 대처다. 규모 없는 자는 권계하고, 마음이 약한 자는 안위하고, 힘이 없는 자는 붙들어 주라. 바울은 누구에게 무엇이 필요한지 구별한다."),
"2th-3-3": dict(
 pt="Vem logo depois da admissão de que nem todos têm fé. A afirmação sobre a fidelidade de Deus é contraposta à pouca confiabilidade das pessoas.",
 it="Viene subito dopo l’ammissione che non tutti hanno la fede. L’affermazione sulla fedeltà di Dio è contrapposta all’inaffidabilità delle persone.",
 ko="모든 사람이 믿음을 가진 것은 아니라는 인정 바로 뒤에 나온다. 주께서 미쁘시다는 말은 사람의 미덥지 못함과 대비된다."),
"1ti-1-15": dict(
 pt="Paulo se chama o principal dos pecadores no presente, não no passado. Depois explica que foi justamente por isso que recebeu misericórdia: como exemplo.",
 it="Paolo si definisce il primo dei peccatori al presente, non al passato. Poi spiega che proprio per questo ha ottenuto misericordia: come esempio.",
 ko="바울은 자신을 과거가 아니라 현재 시제로 죄인 중의 괴수라 부른다. 이어서 바로 그렇기에 본보기로 긍휼을 입었다고 설명한다."),
"2ti-2-13": dict(
 pt="A última linha de um hino cristão antigo que Paulo cita. Das quatro linhas, só ela quebra a simetria: a resposta não é um espelho.",
 it="L’ultima riga di un antico inno cristiano citato da Paolo. Delle quattro righe è l’unica a rompere la simmetria: la risposta non è speculare.",
 ko="바울이 인용하는 초대 그리스도인 찬가의 마지막 줄이다. 네 줄 가운데 이것만 대칭을 깬다. 응답이 거울처럼 되돌아오지 않는다."),
"2ti-4-17": dict(
 pt="Paulo escreve que, na sua primeira audiência, ninguém compareceu e todos o abandonaram. Pede que isso não lhes seja imputado e diz quem esteve ao seu lado.",
 it="Paolo scrive che alla prima udienza del suo processo nessuno venne e tutti lo abbandonarono. Chiede che non venga loro imputato, e dice chi invece gli fu accanto.",
 ko="바울은 처음 변명할 때 아무도 함께하지 않고 다 자기를 버렸다고 쓴다. 그는 그들에게 허물을 돌리지 말기를 구하고, 누가 곁에 섰는지 말한다."),
"heb-2-18": dict(
 pt="O argumento se apoia na experiência: ajuda quem passou por isso. O verbo traduzido como “tentado” aqui significa ser provado ao limite, não seduzido.",
 it="L’argomento si basa sull’esperienza: può aiutare chi ci è passato. Il verbo reso con «tentati» indica qui una prova di resistenza fino al limite, non una seduzione.",
 ko="논거는 경험에 기대고 있다. 직접 겪어 본 이가 도울 수 있다. “시험을 받는”으로 번역된 동사는 유혹이 아니라 한계까지 시험당하는 것을 뜻한다."),
"heb-13-2": dict(
 pt="Uma alusão a Abraão recebendo três viajantes junto aos carvalhos, e a Ló. O ponto é que nenhum dos dois sabia quem estava recebendo; do contrário, o argumento cai.",
 it="Un rimando ad Abramo, che accolse tre viandanti presso le querce, e a Lot. Il punto è che nessuno dei due sapeva chi stesse accogliendo; altrimenti l’argomento non regge.",
 ko="상수리나무 곁에서 세 나그네를 맞은 아브라함과 롯을 가리킨다. 요점은 둘 다 누구를 맞는지 몰랐다는 것이며, 그렇지 않으면 논거가 서지 않는다."),
"jas-2-17": dict(
 pt="Logo antes vem um exemplo: a alguém sem roupa nem comida se diz “ide em paz, aquecei-vos”, e nada lhe é dado. A conclusão sai desse exemplo.",
 it="Poco prima c’è un esempio: a chi è senza vestiti né cibo si dice «andate in pace, scaldatevi» e non gli si dà nulla. La conclusione è tratta da quell’esempio.",
 ko="바로 앞에 예가 나온다. 헐벗고 굶주린 사람에게 “평안히 가라, 덥게 하라”고만 하고 아무것도 주지 않는다. 결론은 이 예에서 나온다."),
"jas-4-6": dict(
 pt="Uma citação de Provérbios feita no meio de uma análise das brigas na comunidade. Tiago explica de onde vêm as contendas e encontra a causa nos desejos.",
 it="Una citazione dai Proverbi, inserita nel mezzo di un’analisi dei litigi nella comunità. Giacomo spiega da dove nascono le liti e ne trova la causa nei desideri.",
 ko="공동체의 다툼을 분석하는 도중에 인용한 잠언의 말씀이다. 야고보는 싸움이 어디서 오는지 설명하고 그 원인을 정욕에서 찾는다."),
"jas-5-7": dict(
 pt="A imagem de um lavrador esperando a chuva. Aquela terra tinha duas estações de chuva, as primeiras e as últimas, e entre elas só restava esperar.",
 it="L’immagine di un contadino che aspetta la pioggia. In quella terra c’erano due stagioni delle piogge, la precoce e la tardiva, e tra le due non restava che aspettare.",
 ko="비를 기다리는 농부의 이미지다. 그 땅에는 이른 비와 늦은 비 두 철이 있었고, 그 사이에는 기다리는 것밖에 할 일이 없었다."),
"1pe-4-8": dict(
 pt="A frase seguinte explica como isso fica na prática: acolher uns aos outros sem murmurar. Eram pessoas que viviam apertadas e pobres.",
 it="La frase successiva spiega come si traduce in pratica: ospitarsi a vicenda senza mormorare. Erano persone che vivevano strette e in povertà.",
 ko="다음 구절이 실제 모습을 풀어 준다. 원망 없이 서로 대접하라는 것이다. 비좁고 가난하게 살던 사람들에게 한 말이다."),
"1pe-5-8": dict(
 pt="Pedro escreve aos perseguidos e acrescenta que o mesmo está acontecendo com seus irmãos no mundo inteiro. O consolo aqui é que eles não estão sozinhos nisso.",
 it="Pietro scrive ai perseguitati e aggiunge che lo stesso accade ai loro fratelli in tutto il mondo. La consolazione qui è che non sono soli in questo.",
 ko="베드로는 박해받는 이들에게, 세상에 있는 형제들도 같은 고난을 당하고 있다고 덧붙인다. 위로는 그들이 혼자가 아니라는 데 있다."),
"1jn-3-20": dict(
 pt="Trata do caso em que o próprio coração acusa a pessoa. João não discute com a acusação; diz que existe um tribunal mais alto que o coração.",
 it="Si tratta del caso in cui è il proprio cuore ad accusare una persona. Giovanni non contesta l’accusa: dice che esiste un tribunale più alto del cuore.",
 ko="자기 마음이 자기를 책망하는 경우에 관한 말이다. 요한은 그 고발과 다투지 않고, 마음보다 더 높은 법정이 있다고 말한다."),
"jud-1-24": dict(
 pt="As últimas linhas de uma carta curta, quase inteiramente dedicada a advertências contra o engano. Ela termina não com uma ameaça, mas com a promessa de amparar alguém.",
 it="Le ultime righe di una lettera breve, quasi interamente dedicata agli avvertimenti contro l’inganno. Non si chiude con una minaccia, ma con la promessa di sostenere.",
 ko="거의 전부가 미혹에 대한 경고로 채워진 짧은 서신의 마지막 구절이다. 편지는 위협이 아니라 넘어지지 않게 지켜 주겠다는 약속으로 끝난다."),
"rev-1-17": dict(
 pt="João escreve que caiu como morto diante da visão. A primeira coisa que ouve não é uma explicação, mas “não temas”, com uma mão pousada sobre ele.",
 it="Giovanni scrive che alla visione cadde ai suoi piedi come morto. La prima cosa che sente non è una spiegazione, ma «non temere», con una mano posata su di lui.",
 ko="요한은 환상을 보고 죽은 자같이 그 발 앞에 엎드러졌다고 쓴다. 그가 처음 들은 것은 설명이 아니라, 자기 위에 얹힌 손과 “두려워 말라”였다."),
"rev-7-17": dict(
 pt="Dito sobre pessoas que vieram da grande tribulação. A imagem é invertida de propósito: o cordeiro é chamado de pastor que conduz às fontes de água.",
 it="Detto di persone uscite dalla grande tribolazione. L’immagine è capovolta di proposito: l’agnello è chiamato pastore che guida alle sorgenti d’acqua.",
 ko="큰 환난에서 나온 사람들에 관한 말이다. 이미지는 일부러 뒤집혀 있다. 어린 양이 생명수 샘으로 인도하는 목자로 불린다."),
"rev-14-13": dict(
 pt="Um dos poucos lugares do livro em que uma voz manda escrever algo à parte. Dito sobre os que morreram sob perseguição: o descanso vem primeiro, e as obras vêm depois.",
 it="Uno dei pochi punti del libro in cui una voce ordina di scrivere qualcosa a parte. Detto di chi è morto nella persecuzione: prima viene il riposo, poi le loro opere li seguono.",
 ko="이 책에서 음성이 따로 기록하라고 명하는 몇 안 되는 곳 가운데 하나다. 박해 속에 죽은 이들에 관한 말로, 쉼이 먼저 나오고 그들의 행한 일이 뒤따른다."),
"rev-22-5": dict(
 pt="A penúltima imagem do livro. A noite é apontada como o que não existirá mais, e com ela a necessidade de uma lâmpada, com a qual tudo começou.",
 it="La penultima immagine del libro. La notte è indicata come ciò che non ci sarà più, e con essa sparisce il bisogno della lampada da cui tutto era cominciato.",
 ko="이 책의 마지막에서 두 번째 장면이다. 밤은 더 이상 없을 것으로 불리며, 그와 함께 이 모든 것의 시작이었던 등불도 필요 없어진다."),
}
