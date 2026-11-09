# -*- coding: utf-8 -*-
"""
Lampada — строки контекста на es, fr, de.

Русский и английский лежат в context_data.py — там источник истины по смыслу.
Здесь только переводы, ключ тот же id отрывка.

Правила те же, что для ru и en: до 34 слов, кто говорит и при каких
обстоятельствах, без толкования и без проповеди. Немецкий длиннее остальных,
поэтому его чаще приходится ужимать — сокращать надо фразу, а не факт.

Заполняется партиями. Незаполненные id сборка показывает как пропуски.
"""

T = {

# ── партия 1 ──────────────────────────────────────────────────────────────
"mat-11-28": dict(
 es="Jesús lo dice en Galilea, a gente agotada por un montón de reglas religiosas. No se dirige a los fuertes, sino a los que ya no pueden más.",
 fr="Jésus le dit en Galilée, à des gens épuisés par une masse de règles religieuses. Il ne s’adresse pas aux forts, mais à ceux qui n’en peuvent plus.",
 de="Jesus sagt das in Galiläa, zu Menschen, die religiöse Vorschriften zermürbt haben. Er spricht nicht die Starken an, sondern die am Ende ihrer Kräfte."),
"psa-23-1": dict(
 es="Salmo de David. Fue pastor antes de ser rey y sabía por dentro lo que cuesta llevar un rebaño por barrancos y encontrarle agua.",
 fr="Psaume de David. Il fut berger avant d’être roi et savait de l’intérieur ce que coûte de mener un troupeau par les ravins et de lui trouver de l’eau.",
 de="Ein Psalm Davids. Er war Hirte, bevor er König wurde, und wusste von innen, was es heißt, eine Herde durch Schluchten zu führen und Wasser zu finden."),
"isa-41-10": dict(
 es="Profecía para un pueblo que teme desaparecer entre imperios mayores. Las palabras no van dirigidas a los valientes, sino a quienes ya entendieron lo pequeños que son.",
 fr="Prophétie pour un peuple qui craint de disparaître parmi de plus grands empires. Ces mots ne s’adressent pas aux courageux, mais à ceux qui ont compris leur petitesse.",
 de="Eine Prophetie für ein Volk, das fürchtet, zwischen größeren Reichen zu verschwinden. Die Worte gelten nicht den Mutigen, sondern denen, die ihre Kleinheit begriffen haben."),
"php-4-6": dict(
 es="Pablo escribe esto bajo custodia, esperando juicio. El hombre que habla de calma no tiene ninguna garantía sobre el día siguiente.",
 fr="Paul écrit ceci sous garde, en attente de jugement. L’homme qui parle de paix n’a aucune garantie sur le lendemain.",
 de="Paulus schreibt das unter Bewachung, während er auf sein Verfahren wartet. Der Mann, der von Ruhe spricht, hat keinerlei Sicherheit für morgen."),
"jer-29-11": dict(
 es="De una carta a los desterrados en Babilonia. Jeremías acaba de decirles que construyan casas y críen hijos: el regreso llegará, pero no pronto, en setenta años.",
 fr="D’une lettre aux exilés de Babylone. Jérémie vient de leur dire de bâtir des maisons et d’élever des enfants : le retour viendra, mais dans soixante-dix ans.",
 de="Aus einem Brief an die Verbannten in Babylon. Jeremia hat ihnen eben gesagt, Häuser zu bauen und Kinder großzuziehen: die Rückkehr kommt, aber erst in siebzig Jahren."),
"rom-8-28": dict(
 es="Pablo escribe a cristianos de Roma que viven bajo sospecha oficial. La frase está en un capítulo sobre el sufrimiento, no sobre la buena suerte.",
 fr="Paul écrit à des chrétiens de Rome vivant sous surveillance officielle. La phrase se trouve dans un chapitre sur la souffrance, non sur la chance.",
 de="Paulus schreibt an Christen in Rom, die unter behördlichem Verdacht leben. Der Satz steht in einem Kapitel über Leiden, nicht über Glück."),
"psa-46-1": dict(
 es="Canto del templo para cantar en asamblea. Sus imágenes vienen del terremoto y del asedio: cosas que los oyentes habían visto, no imaginado.",
 fr="Chant du temple pour l’assemblée. Ses images viennent du tremblement de terre et du siège : des choses que les auditeurs avaient vues, non imaginées.",
 de="Ein Tempellied für die Gemeinde. Seine Bilder stammen von Erdbeben und Belagerung — Dinge, die die Zuhörer selbst gesehen und nicht erdacht hatten."),
"jhn-14-27": dict(
 es="Dicho la noche antes del arresto, en la mesa, a discípulos que aún no saben lo que ocurre. En pocas horas todos se dispersarán.",
 fr="Dit la nuit avant l’arrestation, à table, à des disciples qui ignorent encore ce qui se prépare. En quelques heures, tous se disperseront.",
 de="Gesagt in der Nacht vor der Verhaftung, bei Tisch, zu Jüngern, die noch nicht wissen, was geschieht. Wenige Stunden später laufen sie auseinander."),
"1pe-5-7": dict(
 es="Pedro escribe a cristianos dispersos por Asia Menor cuando empieza la persecución. El consejo viene de un hombre que una vez se quebró y negó conocer a Jesús.",
 fr="Pierre écrit à des chrétiens dispersés en Asie Mineure alors que la persécution commence. Le conseil vient d’un homme qui a craqué et nié connaître Jésus.",
 de="Petrus schreibt an Christen in Kleinasien, als die Verfolgung beginnt. Der Rat kommt von einem Mann, der einmal zusammenbrach und leugnete, Jesus zu kennen."),
"pro-3-5": dict(
 es="De una colección de instrucciones que un padre da a su hijo. Sabiduría práctica, escrita para un joven que va a empezar a decidir por sí mismo.",
 fr="D’un recueil d’instructions qu’un père donne à son fils. Sagesse pratique, écrite pour un jeune homme qui va commencer à décider seul.",
 de="Aus einer Sammlung von Anweisungen, die ein Vater seinem Sohn gibt. Praktische Weisheit für einen jungen Mann, der eigene Entscheidungen zu treffen beginnt."),
"isa-40-31": dict(
 es="Comienzo del libro del consuelo. El profeta habla a desterrados agotados de esperar el regreso, a gente cuyas fuerzas se han acabado.",
 fr="Ouverture du livre de la consolation. Le prophète parle à des exilés épuisés d’attendre le retour, à des gens à bout de forces.",
 de="Der Anfang des Trostbuches. Der Prophet spricht zu Verbannten, die das Warten auf die Rückkehr zermürbt hat — zu Menschen ohne Kraft."),
"psa-34-18": dict(
 es="Salmo de David. Su encabezado lo vincula al tiempo en que huía de la muerte y fingió locura para sobrevivir.",
 fr="Psaume de David. Son titre le rattache au temps où il fuyait la mort et feignit la folie pour survivre.",
 de="Ein Psalm Davids. Seine Überschrift verbindet ihn mit der Zeit, als er dem Tod entfloh und Wahnsinn vortäuschte, um zu überleben."),
"mat-5-4": dict(
 es="Del Sermón del Monte, dado en una ladera junto al mar de Galilea. Los primeros oyentes eran gente sin dinero ni posición, que había ido a pie.",
 fr="Du Sermon sur la montagne, donné sur une colline au bord du lac de Galilée. Les premiers auditeurs étaient des gens sans argent ni rang, venus à pied.",
 de="Aus der Bergpredigt, gehalten an einem Hang am See Genezareth. Die ersten Zuhörer waren Menschen ohne Geld und Ansehen, die zu Fuß gekommen waren."),
"rev-21-4": dict(
 es="Juan escribe esto desterrado en Patmos, para iglesias donde matan a la gente por su fe. Trata de cómo termina todo.",
 fr="Jean écrit ceci en exil à Patmos, pour des Églises où l’on tue des gens à cause de leur foi. Il s’agit de la fin de tout.",
 de="Johannes schreibt das in der Verbannung auf Patmos, für Gemeinden, in denen Menschen ihres Glaubens wegen getötet werden. Es geht darum, wie alles endet."),
"lam-3-22": dict(
 es="Escrito sobre las ruinas de Jerusalén, tras el asedio y el hambre. Las palabras sobre la fidelidad vienen de un hombre que acaba de enterrar su ciudad.",
 fr="Écrit sur les ruines de Jérusalem, après le siège et la famine. Les mots sur la fidélité viennent d’un homme qui vient d’enterrer sa ville.",
 de="Geschrieben über den Trümmern Jerusalems, nach Belagerung und Hunger. Die Worte über Treue stammen von einem Mann, der gerade seine Stadt begraben hat."),
"1th-5-16": dict(
 es="De la carta más antigua de Pablo, a una comunidad de pocos meses. Instrucciones breves al final de la carta, casi en forma de lista.",
 fr="De la plus ancienne lettre de Paul, à une communauté vieille de quelques mois. Brèves instructions en fin de lettre, presque sous forme de liste.",
 de="Aus dem frühesten Brief des Paulus, an eine erst wenige Monate alte Gemeinde. Kurze Anweisungen am Briefende, fast wie eine Liste."),
"psa-118-24": dict(
 es="Canto de acción de gracias que se entonaba en las fiestas junto al templo. Se leía en Pascua y, según los Evangelios, Jesús lo cantó antes del arresto.",
 fr="Chant d’action de grâce entonné aux fêtes près du temple. On le lisait à la Pâque et, selon les Évangiles, Jésus le chanta avant son arrestation.",
 de="Ein Danklied, das man an den Festen beim Tempel sang. Es wurde zu Passa gelesen, und laut den Evangelien sang Jesus es vor seiner Verhaftung."),
"col-3-13": dict(
 es="Pablo escribe desde la cárcel a una ciudad que nunca ha visitado. Habla de personas que tendrán que convivir todos los días.",
 fr="Paul écrit de prison à une ville qu’il n’a jamais visitée. Il parle de gens qui devront vivre côte à côte chaque jour.",
 de="Paulus schreibt aus dem Gefängnis an eine Stadt, die er nie besucht hat. Er spricht von Menschen, die täglich miteinander auskommen müssen."),
"eph-4-32": dict(
 es="De una carta a Éfeso, ciudad portuaria donde los cristianos eran una pequeña comunidad mixta de judíos y griegos acostumbrados a mantenerse aparte.",
 fr="D’une lettre à Éphèse, ville portuaire où les chrétiens formaient une petite communauté mêlée de Juifs et de Grecs habitués à se tenir à l’écart.",
 de="Aus einem Brief nach Ephesus, einer Hafenstadt, wo die Christen eine kleine gemischte Gemeinde aus Juden und Griechen waren, die einander sonst mieden."),
"mat-6-14": dict(
 es="Del Sermón del Monte, justo después del padrenuestro. Explica la frase sobre las deudas que los oyentes acaban de escuchar.",
 fr="Du Sermon sur la montagne, juste après le Notre Père. Cela explique la phrase sur les dettes que les auditeurs viennent d’entendre.",
 de="Aus der Bergpredigt, direkt nach dem Vaterunser. Es erklärt den Satz über die Schulden, den die Zuhörer eben gehört haben."),
"mrk-9-24": dict(
 es="Lo dice el padre de un niño enfermo a quien los discípulos no pudieron curar. No es teólogo ni discute: ha dejado de fingir que su fe es firme.",
 fr="Dit par le père d’un enfant malade que les disciples n’avaient pas su guérir. Il n’est pas théologien et ne discute pas : il cesse de feindre une foi solide.",
 de="Gesagt vom Vater eines kranken Jungen, den die Jünger nicht heilen konnten. Er ist kein Theologe und streitet nicht — er hört auf, festen Glauben vorzutäuschen."),
"jhn-20-29": dict(
 es="Dicho a Tomás una semana después de la resurrección. Se había negado a creer a los demás y exigió tocar las heridas, y se le dio la ocasión.",
 fr="Dit à Thomas une semaine après la résurrection. Il avait refusé de croire les autres et exigé de toucher les plaies : l’occasion lui fut donnée.",
 de="Gesagt zu Thomas eine Woche nach der Auferstehung. Er hatte den anderen nicht geglaubt und verlangt, die Wunden zu berühren — und bekam die Gelegenheit."),
"jos-1-9": dict(
 es="Dicho a Josué cuando toma el mando tras la muerte de Moisés. Un hombre que pasó cuarenta años como segundo debe ir primero por vez primera.",
 fr="Dit à Josué au moment où il prend la tête du peuple après la mort de Moïse. Quarante ans second, il doit pour la première fois marcher devant.",
 de="Gesagt zu Josua, als er nach dem Tod des Mose die Führung übernimmt. Vierzig Jahre lang Zweiter, muss er zum ersten Mal vorangehen."),
"php-4-13": dict(
 es="Pablo escribe bajo custodia, y la frase anterior explica lo que quiere decir: ha aprendido a vivir tanto en la abundancia como en la escasez.",
 fr="Paul écrit sous garde, et la phrase précédente explique ce qu’il entend : il a appris à vivre dans l’abondance comme dans le dénuement.",
 de="Paulus schreibt unter Bewachung, und der Satz davor erklärt, was er meint: er hat gelernt, im Überfluss wie im Mangel zu leben."),
"deu-31-6": dict(
 es="Último discurso de Moisés. Tiene ciento veinte años, no entrará él mismo en la tierra prometida, y dice esto a quienes irán sin él.",
 fr="Dernier discours de Moïse. Il a cent vingt ans, n’entrera pas lui-même dans la terre promise, et dit cela à ceux qui iront sans lui.",
 de="Die letzte Rede des Mose. Er ist hundertzwanzig, wird das verheißene Land selbst nicht betreten und sagt das zu denen, die ohne ihn gehen."),
"psa-4-8": dict(
 es="Salmo vespertino de David. En las líneas anteriores se queja de gente que lo calumnia, y aun así se acuesta a dormir.",
 fr="Psaume du soir de David. Dans les lignes précédentes il se plaint de gens qui le calomnient, et il se couche quand même.",
 de="Ein Abendpsalm Davids. In den Zeilen davor klagt er über Menschen, die ihn verleumden — und legt sich trotzdem schlafen."),
"psa-121-3": dict(
 es="Cántico de las subidas, cantado por peregrinos camino de Jerusalén, que dormían al raso en un camino donde asaltaban a los viajeros.",
 fr="Cantique des montées, chanté par les pèlerins sur la route de Jérusalem, dormant à la belle étoile sur un chemin où l’on détroussait les voyageurs.",
 de="Ein Wallfahrtslied, gesungen von Pilgern auf dem Weg nach Jerusalem, die im Freien schliefen — auf einer Straße, auf der Reisende ausgeraubt wurden."),
"mat-6-34": dict(
 es="Del Sermón del Monte. Justo antes, Jesús habla de las aves y de los lirios silvestres: sus oyentes no tenían asegurada la comida del día siguiente.",
 fr="Du Sermon sur la montagne. Juste avant, Jésus parle des oiseaux et des lis des champs : ses auditeurs n’avaient pas la nourriture du lendemain assurée.",
 de="Aus der Bergpredigt. Kurz davor spricht Jesus von den Vögeln und den Lilien des Feldes — seine Zuhörer hatten das Essen von morgen nicht sicher."),
"psa-119-105": dict(
 es="Del salmo más largo del Salterio, un acróstico según el alfabeto hebreo. La lámpara es un candil de barro que alumbraba un paso, no el camino entero.",
 fr="Du plus long psaume du Psautier, un acrostiche sur l’alphabet hébreu. La lampe est une petite lampe à huile en terre qui éclairait un pas, non la route.",
 de="Aus dem längsten Psalm des Psalters, einem Akrostichon nach dem hebräischen Alphabet. Die Leuchte ist eine kleine Tonöllampe, die einen Schritt erhellte, nicht den Weg."),
"jhn-3-16": dict(
 es="De una conversación nocturna con Nicodemo, miembro del consejo que vino en secreto para que no lo vieran con Jesús.",
 fr="D’un entretien nocturne avec Nicodème, membre du conseil venu en secret pour qu’on ne le voie pas avec Jésus.",
 de="Aus einem nächtlichen Gespräch mit Nikodemus, einem Ratsmitglied, das heimlich kam, um nicht mit Jesus gesehen zu werden."),
"2co-12-9": dict(
 es="Pablo acaba de describir una enfermedad o defecto del que pidió tres veces ser librado, y no lo fue. Esta es la respuesta que recibió.",
 fr="Paul vient de décrire une maladie ou une infirmité dont il a demandé trois fois d’être délivré, sans l’être. Voici la réponse qu’il a reçue.",
 de="Paulus hat gerade ein Leiden beschrieben, von dem er dreimal befreit werden wollte — und nicht wurde. Das ist die Antwort, die er bekam."),
"heb-11-1": dict(
 es="Comienzo de un capítulo que luego enumera a personas que murieron sin ver lo prometido. La definición va antes de esa lista, no después.",
 fr="Ouverture d’un chapitre qui énumère ensuite des gens morts sans avoir vu la promesse. La définition précède cette liste, elle ne la suit pas.",
 de="Der Anfang eines Kapitels, das danach Menschen aufzählt, die starben, ohne das Verheißene zu sehen. Die Definition steht vor dieser Liste, nicht danach."),
"psa-139-14": dict(
 es="Salmo de David sobre que no hay dónde esconderse de Dios. La línea sobre cómo está hecho el hombre está junto a otras sobre estar siempre a la vista.",
 fr="Psaume de David sur l’impossibilité de se cacher de Dieu. La ligne sur la façon dont l’homme est fait voisine celles sur le fait d’être toujours vu.",
 de="Ein Psalm Davids darüber, dass es kein Versteck vor Gott gibt. Die Zeile darüber, wie ein Mensch gemacht ist, steht neben Zeilen übers Gesehenwerden."),
"isa-43-2": dict(
 es="Profecía a un pueblo que vivió la deportación. El agua y el fuego no son metáforas generales: detrás están el paso del mar y los incendios de la guerra.",
 fr="Prophétie à un peuple qui a vécu la déportation. L’eau et le feu ne sont pas des métaphores : derrière eux, le passage de la mer et les incendies de guerre.",
 de="Eine Prophetie an ein Volk, das die Deportation erlebt hat. Wasser und Feuer sind keine allgemeinen Bilder: dahinter stehen der Meerdurchzug und die Brände des Krieges."),
"gal-6-9": dict(
 es="Final de una carta dura a los gálatas, donde Pablo discute con ellos casi todo el tiempo. Al despedirse habla del cansancio, no de tener razón.",
 fr="Fin d’une lettre sévère aux Galates, où Paul les querelle presque tout du long. En prenant congé, il parle de fatigue, non d’avoir raison.",
 de="Das Ende eines scharfen Briefes an die Galater, in dem Paulus fast durchgehend mit ihnen streitet. Zum Abschied spricht er von Müdigkeit, nicht vom Rechthaben."),
"gen-1-27": dict(
 es="Primera página de la Biblia, el relato de la creación. Se dice de todo ser humano a la vez, antes de cualquier división por pueblos, rangos o méritos.",
 fr="Première page de la Bible, le récit de la création. Cela est dit de tout être humain à la fois, avant toute division en peuples, rangs ou mérites.",
 de="Die erste Seite der Bibel, der Schöpfungsbericht. Es gilt allen Menschen zugleich, vor jeder Einteilung nach Völkern, Rängen oder Verdiensten."),
"gen-28-15": dict(
 es="Jacob duerme en un lugar vacío, huyendo de un hermano que ha jurado matarlo. Sueña con una escalera y oye esto dentro del sueño.",
 fr="Jacob dort dans un lieu désert, fuyant un frère qui a juré de le tuer. Il rêve d’un escalier et entend cela dans le rêve.",
 de="Jakob schläft an einem leeren Ort, auf der Flucht vor einem Bruder, der geschworen hat, ihn zu töten. Er träumt von einer Treppe und hört das im Traum."),
"gen-50-20": dict(
 es="José se lo dice a los hermanos que lo vendieron como esclavo. Su padre acaba de morir y temen que ahora se vengue.",
 fr="Joseph le dit aux frères qui l’ont vendu comme esclave. Leur père vient de mourir et ils craignent qu’il ne se venge.",
 de="Josef sagt das zu den Brüdern, die ihn einst in die Sklaverei verkauft haben. Ihr Vater ist eben gestorben, und sie fürchten seine Rache."),
"exo-14-14": dict(
 es="El pueblo está atrapado entre el mar y los carros que lo persiguen. Es la respuesta de Moisés a una multitud que ya grita que la esclavitud era mejor.",
 fr="Le peuple est pris entre la mer et les chars lancés à sa poursuite. C’est la réponse de Moïse à une foule qui crie déjà que l’esclavage valait mieux.",
 de="Das Volk sitzt zwischen dem Meer und den verfolgenden Streitwagen fest. Das ist die Antwort des Mose auf eine Menge, die schon die Sklaverei zurückwünscht."),
"exo-33-14": dict(
 es="Moisés discute con Dios tras el becerro de oro y se niega a seguir guiando solo al pueblo. Esta es la respuesta a su negativa.",
 fr="Moïse discute avec Dieu après le veau d’or et refuse de conduire seul le peuple plus loin. Voici la réponse à son refus.",
 de="Mose streitet nach dem Goldenen Kalb mit Gott und weigert sich, das Volk allein weiterzuführen. Das ist die Antwort auf seine Weigerung."),
"num-6-24": dict(
 es="Fórmula de bendición con que los sacerdotes despedían al pueblo. Se pronunciaba en voz alta sobre ellos y es de las oraciones más antiguas de Israel.",
 fr="Formule de bénédiction par laquelle les prêtres congédiaient le peuple. Elle était dite à voix haute sur eux et compte parmi les plus anciennes prières d’Israël.",
 de="Die Segensformel, mit der die Priester das Volk entließen. Sie wurde laut über die Menschen gesprochen und gehört zu den ältesten Gebeten Israels."),
"deu-6-5": dict(
 es="Palabras que en el judaísmo se recitan dos veces al día y se escriben en las jambas. Moisés las da al pueblo antes de entrar en la tierra nueva.",
 fr="Paroles récitées deux fois par jour dans le judaïsme et inscrites sur les montants des portes. Moïse les donne au peuple avant l’entrée dans le pays.",
 de="Worte, die im Judentum zweimal täglich gesprochen und an die Türpfosten geschrieben werden. Mose gibt sie dem Volk vor dem Einzug ins neue Land."),
"jos-24-15": dict(
 es="Josué reúne al pueblo al final de su vida y lo obliga a elegir abiertamente. Muchos en esa asamblea aún guardan dioses antiguos en casa.",
 fr="Josué rassemble le peuple à la fin de sa vie et le force à choisir ouvertement. Beaucoup dans cette assemblée gardent encore d’anciens dieux chez eux.",
 de="Josua versammelt das Volk am Ende seines Lebens und zwingt es zu offener Wahl. Viele in dieser Versammlung haben zu Hause noch alte Götter stehen."),
"1sa-16-7": dict(
 es="El profeta Samuel elige rey entre los hijos de Isaí y está a punto de ungir al más alto. A David ni siquiera lo han llamado.",
 fr="Le prophète Samuel choisit un roi parmi les fils d’Isaï et s’apprête à oindre le plus grand. David n’a même pas été appelé.",
 de="Der Prophet Samuel wählt unter den Söhnen Isais einen König und will gerade den Größten salben. David ist noch nicht einmal geholt worden."),
"1ki-19-11": dict(
 es="Elías huye al desierto tras las amenazas de la reina y pide morir. Espera a Dios en el viento, el terremoto y el fuego, y no lo halla en ninguno.",
 fr="Élie fuit au désert après les menaces de la reine et demande à mourir. Il attend Dieu dans le vent, le tremblement de terre et le feu, sans l’y trouver.",
 de="Elia flieht nach den Drohungen der Königin in die Wüste und bittet zu sterben. Er wartet auf Gott in Sturm, Beben und Feuer — und findet ihn in keinem."),
"2ch-20-12": dict(
 es="El rey Josafat ora en voz alta ante todo el pueblo mientras tres ejércitos convergen sobre la ciudad. Reconoce abiertamente que no tiene ningún plan.",
 fr="Le roi Josaphat prie à voix haute devant tout le peuple alors que trois armées convergent vers la ville. Il admet ouvertement n’avoir aucun plan.",
 de="König Joschafat betet laut vor dem ganzen Volk, während drei Heere auf die Stadt zumarschieren. Er gibt offen zu, dass er keinen Plan hat."),
"neh-8-10": dict(
 es="El pueblo oye leer la ley por primera vez en décadas y llora. Nehemías detiene el llanto: es día de fiesta, y les manda comer y compartir.",
 fr="Le peuple entend lire la loi pour la première fois depuis des décennies et pleure. Néhémie arrête les pleurs : c’est jour de fête, il leur dit de manger.",
 de="Das Volk hört zum ersten Mal seit Jahrzehnten das Gesetz vorlesen und weint. Nehemia stoppt das Weinen: es ist Festtag, sie sollen essen und teilen."),
"job-19-25": dict(
 es="Job lo dice tras perder a sus hijos, sus bienes y su salud, en medio de una discusión con amigos que insisten en que la culpa es suya.",
 fr="Job le dit après avoir perdu ses enfants, ses biens et sa santé, au milieu d’une dispute avec des amis qui soutiennent que c’est sa faute.",
 de="Hiob sagt das, nachdem er Kinder, Besitz und Gesundheit verloren hat, mitten im Streit mit Freunden, die auf seiner eigenen Schuld beharren."),
"job-42-5": dict(
 es="Final del libro. Dios nunca explica a Job por qué ocurrió todo aquello, pero sí habla con él. Esta es la respuesta de Job a la conversación.",
 fr="Fin du livre. Dieu n’explique jamais à Job pourquoi tout cela est arrivé, mais il lui parle. Voici la réponse de Job à cet entretien.",
 de="Das Ende des Buches. Gott erklärt Hiob nie, warum all das geschah, spricht aber mit ihm. Das ist Hiobs Antwort auf dieses Gespräch."),
"psa-1-1": dict(
 es="Salmo que abre todo el Salterio. Está primero como una puerta: después vienen cantos de alegría, de ira y de desesperación, y este marca la bifurcación.",
 fr="Psaume qui ouvre tout le Psautier. Il est placé en tête comme une porte : suivent des chants de joie, de colère et de détresse ; celui-ci pose le choix.",
 de="Der Psalm, der den ganzen Psalter eröffnet. Er steht als Tür am Anfang: danach folgen Lieder der Freude, des Zorns und der Verzweiflung — dieser stellt die Weiche."),
"psa-16-11": dict(
 es="Salmo de David escrito en peligro: en sus primeras líneas pide ser guardado. Las palabras sobre la alegría están al final de esa misma oración.",
 fr="Psaume de David écrit dans le danger : dans ses premières lignes il demande d’être gardé. Les mots sur la joie viennent à la fin de la même prière.",
 de="Ein Psalm Davids, in Gefahr geschrieben: in den ersten Zeilen bittet er um Bewahrung. Die Worte über die Freude stehen am Ende desselben Gebets."),
"psa-19-1": dict(
 es="Salmo de David que pone cielo y ley uno junto al otro como dos modos de conocer lo mismo. La primera mitad trata de estrellas; la segunda, de mandamientos.",
 fr="Psaume de David qui met le ciel et la loi côte à côte comme deux façons de connaître la même chose. La première moitié parle d’étoiles, la seconde de commandements.",
 de="Ein Psalm Davids, der Himmel und Gesetz nebeneinanderstellt als zwei Wege, dasselbe zu erkennen. Die erste Hälfte handelt von Sternen, die zweite von Geboten."),
"psa-27-1": dict(
 es="Salmo de David escrito bajo amenaza militar. Luz y fortaleza son aquí palabras del vocabulario de una ciudad sitiada, no abstracciones.",
 fr="Psaume de David écrit sous menace militaire. Lumière et forteresse sont ici des mots du vocabulaire d’une ville assiégée, non des abstractions.",
 de="Ein Psalm Davids, unter militärischer Bedrohung geschrieben. Licht und Feste sind hier Wörter aus dem Alltag einer belagerten Stadt, keine Abstraktionen."),
"psa-27-14": dict(
 es="Línea final de un salmo que empieza con seguridad y a la mitad se quiebra en una súplica de no ser abandonado. La espera es donde acaba.",
 fr="Dernière ligne d’un psaume qui commence avec assurance et bascule à mi-chemin en supplication de n’être pas abandonné. L’attente est le point d’arrivée.",
 de="Die Schlusszeile eines Psalms, der zuversichtlich beginnt und in der Mitte in die Bitte umschlägt, nicht verlassen zu werden. Beim Warten endet er."),
"psa-30-5": dict(
 es="Canto para la dedicación de una casa, escrito tras una enfermedad grave. David habla de una noche que acaba de atravesar, no de la de otro.",
 fr="Chant pour la dédicace d’une maison, écrit après une grave maladie. David parle d’une nuit qu’il vient de traverser, non de celle d’un autre.",
 de="Ein Lied zur Einweihung eines Hauses, nach schwerer Krankheit geschrieben. David spricht von einer Nacht, die er selbst gerade durchlebt hat."),
"psa-32-7": dict(
 es="Salmo sobre reconocer la culpa. En las líneas anteriores David describe cómo calló lo que había hecho y cómo se le secaban los huesos.",
 fr="Psaume sur l’aveu de la faute. Dans les lignes précédentes, David décrit comment il a tu son acte et comment ses os se desséchaient.",
 de="Ein Psalm über das Eingestehen von Schuld. In den Zeilen davor beschreibt David, wie er die Tat verschwieg und wie seine Knochen darüber verdorrten."),
"psa-37-4": dict(
 es="Salmo de David escrito en la vejez, como él mismo dice más abajo. Su tema es por qué a los deshonestos parece irles mejor.",
 fr="Psaume de David écrit dans la vieillesse, comme il le dit plus loin. Son sujet est pourquoi les malhonnêtes semblent mieux s’en tirer.",
 de="Ein Psalm Davids, im Alter geschrieben, wie er weiter unten selbst sagt. Sein Thema ist, warum es Unehrlichen scheinbar besser geht."),
"psa-42-5": dict(
 es="Salmo de un hombre apartado del templo que recuerda cómo iba allí entre la multitud. Habla consigo mismo porque no hay nadie más.",
 fr="Psaume d’un homme coupé du temple, se rappelant comment il y allait dans la foule. Il se parle à lui-même parce qu’il n’y a personne d’autre.",
 de="Der Psalm eines Mannes, der vom Tempel abgeschnitten ist und sich erinnert, wie er in der Menge dorthin ging. Er spricht mit sich selbst, weil niemand da ist."),
"psa-51-10": dict(
 es="El encabezado liga este salmo al peor episodio de la vida de David: después de Betsabé y del asesinato de su marido, cuando el profeta vino a acusarlo.",
 fr="Le titre rattache ce psaume au pire épisode de la vie de David : après Bethsabée et le meurtre de son mari, quand le prophète vint le confondre.",
 de="Die Überschrift bindet diesen Psalm an die schlimmste Episode in Davids Leben: nach Batseba und der Tötung ihres Mannes, als der Prophet ihn stellte."),
"psa-55-22": dict(
 es="Salmo sobre la traición de un amigo cercano: más arriba David escribe que no es un enemigo quien lo insulta, sino alguien con quien iba al templo.",
 fr="Psaume sur la trahison d’un ami proche : plus haut, David écrit que ce n’est pas un ennemi qui l’insulte, mais celui avec qui il allait au temple.",
 de="Ein Psalm über den Verrat eines nahen Freundes: weiter oben schreibt David, es sei kein Feind, der ihn schmäht, sondern einer, mit dem er zum Tempel ging."),
"psa-56-3": dict(
 es="El encabezado sitúa este salmo cuando David cayó en manos filisteas en Gat. Está escrito no después del rescate, sino dentro del miedo.",
 fr="Le titre situe ce psaume au moment où David tomba aux mains des Philistins à Gath. Il est écrit non après la délivrance, mais dans la peur même.",
 de="Die Überschrift verortet diesen Psalm in der Zeit, als David den Philistern in Gat in die Hände fiel. Er ist nicht nach der Rettung geschrieben, sondern mitten in der Angst."),
"psa-62-1": dict(
 es="Salmo de David escrito bajo la presión de gente que, según él, bendice con la boca y maldice por dentro.",
 fr="Psaume de David écrit sous la pression de gens qui, selon lui, bénissent de la bouche et maudissent au-dedans.",
 de="Ein Psalm Davids, geschrieben unter dem Druck von Menschen, die, wie er sagt, mit dem Mund segnen und im Innern fluchen."),
"psa-63-1": dict(
 es="El encabezado sitúa este salmo en el desierto de Judá, adonde David había huido. La sed no es una figura: lo escribió sin agua alrededor.",
 fr="Le titre situe ce psaume dans le désert de Juda, où David avait fui. La soif n’est pas une image : il l’a écrit sans eau autour de lui.",
 de="Die Überschrift verortet diesen Psalm in der Wüste Juda, wohin David geflohen war. Der Durst ist kein Bild: er schrieb ihn ohne Wasser ringsum."),
"psa-73-26": dict(
 es="Salmo de un hombre que reconoce que casi pierde la fe envidiando el bienestar de quienes viven sin honradez. Aquí termina su razonamiento.",
 fr="Psaume d’un homme qui avoue avoir failli perdre la foi en enviant l’aisance de ceux qui vivent malhonnêtement. C’est là que s’achève son raisonnement.",
 de="Der Psalm eines Mannes, der zugibt, fast den Glauben verloren zu haben, weil er den Wohlstand Unehrlicher beneidete. Hier endet sein Gedankengang."),
"psa-84-11": dict(
 es="Canto de peregrino que añora el templo. Dice que preferiría estar en su umbral antes que morar en tiendas de impiedad: compara puertas, no ideas.",
 fr="Chant de pèlerin qui languit après le temple. Il dit préférer le seuil de la maison de Dieu aux tentes de l’impiété : il compare des portes, pas des idées.",
 de="Das Lied eines Pilgers, der sich nach dem Tempel sehnt. Lieber an der Schwelle stehen als in den Zelten des Frevels wohnen — er vergleicht Türen, keine Ideen."),
"psa-90-12": dict(
 es="El único salmo encabezado con el nombre de Moisés. Trata de lo breve que es la vida humana, y la petición aquí es aprender a contar los días.",
 fr="Le seul psaume portant le nom de Moïse. Il parle de la brièveté de la vie humaine, et la demande ici est d’apprendre à compter les jours.",
 de="Der einzige Psalm mit dem Namen des Mose. Er handelt davon, wie kurz eine Lebensspanne ist, und bittet darum, die Tage zählen zu lernen."),
"psa-91-1": dict(
 es="Salmo sobre la protección, que enumera peligros muy concretos de su tiempo: el terror nocturno, la flecha de día y la peste.",
 fr="Psaume sur la protection, qui énumère des dangers très concrets de son temps : la terreur de la nuit, la flèche du jour et la peste.",
 de="Ein Psalm über Schutz, der sehr konkrete Gefahren seiner Zeit aufzählt: den Schrecken der Nacht, den Pfeil am Tag und die Pest."),
"psa-91-11": dict(
 es="Salmo sobre vivir al amparo del Altísimo. La promesa de los ángeles se dice de un camino corriente: no golpearse el pie contra una piedra.",
 fr="Psaume sur la vie à l’abri du Très-Haut. La promesse des anges vise une route ordinaire : ne pas heurter du pied contre une pierre.",
 de="Ein Psalm über das Leben im Schutz des Höchsten. Die Zusage über die Engel gilt einem ganz gewöhnlichen Weg: den Fuß nicht an einen Stein zu stoßen."),
"psa-94-19": dict(
 es="Salmo que se queja de quienes aplastan a viudas y huérfanos seguros de que quedarán impunes. La línea sobre el consuelo está dentro de la queja.",
 fr="Psaume qui se plaint de ceux qui écrasent veuves et orphelins, sûrs de rester impunis. La ligne sur la consolation se tient à l’intérieur de la plainte.",
 de="Ein Psalm, der über jene klagt, die Witwen und Waisen zermalmen und sicher sind, ungestraft davonzukommen. Die Zeile über den Trost steht mitten in der Klage."),
"psa-100-4": dict(
 es="Salmo breve para entrar en el templo, cantado mientras se cruzaban literalmente las puertas hacia el atrio. De ahí las puertas del texto.",
 fr="Bref psaume pour entrer au temple, chanté en franchissant littéralement les portes vers le parvis. D’où les portes dans le texte.",
 de="Ein kurzer Psalm für den Eintritt in den Tempel, gesungen beim buchstäblichen Durchschreiten der Tore zum Vorhof. Daher die Tore im Text."),
"psa-103-2": dict(
 es="Salmo de David que empieza dirigiéndose a sí mismo: ordena a su propia alma no olvidar. Todo lo que sigue es la respuesta a esa orden.",
 fr="Psaume de David qui s’ouvre en s’adressant à lui-même : il ordonne à sa propre âme de ne pas oublier. Tout ce qui suit répond à cet ordre.",
 de="Ein Psalm Davids, der damit beginnt, dass er sich selbst anspricht: er befiehlt seiner eigenen Seele, nicht zu vergessen. Alles Folgende antwortet darauf."),
"psa-107-1": dict(
 es="Salmo para los que volvieron del destierro. Está construido como un pase de lista de rescatados: cada grupo cuenta lo suyo y una línea se repite.",
 fr="Psaume pour ceux qui revinrent d’exil. Il est bâti comme un appel des rescapés : chaque groupe raconte son histoire, et une même ligne revient.",
 de="Ein Psalm für die aus dem Exil Zurückgekehrten. Er ist als Namensaufruf der Geretteten gebaut: jede Gruppe erzählt ihre Geschichte, und eine Zeile kehrt wieder."),
"psa-116-1": dict(
 es="Salmo de un hombre que estuvo a punto de morir y sobrevivió. Dice que invocará a Dios toda su vida porque una vez lo escuchó.",
 fr="Psaume d’un homme qui fut au bord de la mort et survécut. Il dit qu’il invoquera Dieu toute sa vie parce qu’une fois il l’a écouté.",
 de="Der Psalm eines Mannes, der dem Tod nahe war und überlebte. Er sagt, er werde Gott sein Leben lang anrufen, weil dieser einmal zugehört hat."),
"psa-126-5": dict(
 es="Cántico de las subidas sobre el regreso del destierro. La imagen viene del campo: el último grano se sembraba en año de hambre sin certeza de cosecha.",
 fr="Cantique des montées sur le retour d’exil. L’image vient des champs : le dernier grain était semé en année de famine, sans certitude de récolte.",
 de="Ein Wallfahrtslied über die Rückkehr aus dem Exil. Das Bild kommt vom Feld: das letzte Korn wurde im Hungerjahr gesät, ohne Gewissheit einer Ernte."),
"psa-127-2": dict(
 es="Cántico de las subidas encabezado con el nombre de Salomón. Trata de lo inútil de agotarse trabajando, dicho por quien construyó el templo y el palacio.",
 fr="Cantique des montées portant le nom de Salomon. Il parle de l’inutilité de s’épuiser au travail, dit par celui qui bâtit le temple et le palais.",
 de="Ein Wallfahrtslied mit dem Namen Salomos. Es handelt von der Vergeblichkeit, sich zu Tode zu arbeiten — gesagt von dem, der Tempel und Palast baute."),
"psa-130-1": dict(
 es="Cántico de las subidas que empieza desde el fondo. El hebreo para profundidades es agua en la que uno se ahoga; los peregrinos lo cantaban subiendo.",
 fr="Cantique des montées qui commence tout au fond. En hébreu, les profondeurs désignent l’eau où l’on se noie ; les pèlerins le chantaient en montant.",
 de="Ein Wallfahrtslied, das ganz unten beginnt. Das hebräische Wort für Tiefen meint Wasser, in dem man ertrinkt; Pilger sangen es auf dem Weg hinauf."),
"psa-133-1": dict(
 es="Cántico de las subidas que se cantaba cuando parientes de todo el país confluían en Jerusalén para una fiesta y convivían varios días.",
 fr="Cantique des montées chanté quand des parents venus de tout le pays convergeaient vers Jérusalem pour une fête et vivaient ensemble plusieurs jours.",
 de="Ein Wallfahrtslied, gesungen, wenn Verwandte aus dem ganzen Land zu einem Fest in Jerusalem zusammenkamen und mehrere Tage beieinander wohnten."),
"psa-136-1": dict(
 es="Salmo cantado a coros alternos: el sacerdote leía una línea y el pueblo respondía con el estribillo. El estribillo se repite veintiséis veces seguidas.",
 fr="Psaume chanté en alternance : le prêtre lisait une ligne, le peuple répondait par le refrain. Le refrain revient vingt-six fois de suite.",
 de="Ein Psalm im Wechselgesang: ein Priester las eine Zeile, das Volk antwortete mit dem Kehrvers. Der Kehrvers wiederholt sich sechsundzwanzigmal hintereinander."),
"psa-143-8": dict(
 es="Salmo de David escrito cuando un enemigo, según sus palabras, había aplastado su vida contra el suelo. La petición de la mañana viene de una noche sin fin.",
 fr="Psaume de David écrit quand un ennemi avait, selon ses mots, écrasé sa vie contre terre. La demande du matin vient d’une nuit qui n’a pas fini.",
 de="Ein Psalm Davids, geschrieben, als ein Feind ihm nach seinen Worten das Leben zu Boden getreten hatte. Die Bitte um den Morgen kommt aus einer endlosen Nacht."),
"psa-145-18": dict(
 es="Último salmo de David en el Salterio y acróstico según el alfabeto hebreo. Su tema es que el acceso está abierto a todos, no a unos pocos elegidos.",
 fr="Dernier psaume de David dans le Psautier et acrostiche sur l’alphabet hébreu. Son sujet est que l’accès est ouvert à tous, non à quelques élus.",
 de="Davids letzter Psalm im Psalter und ein Akrostichon nach dem hebräischen Alphabet. Sein Thema ist, dass der Zugang allen offensteht, nicht wenigen Auserwählten."),
"psa-147-3": dict(
 es="Salmo escrito tras el regreso del destierro y la reconstrucción de las murallas de Jerusalén. La línea sobre los corazones rotos está junto a otra sobre las estrellas.",
 fr="Psaume écrit après le retour d’exil et la reconstruction des murailles de Jérusalem. La ligne sur les cœurs brisés voisine une ligne sur les étoiles.",
 de="Ein Psalm nach der Rückkehr aus dem Exil und dem Wiederaufbau der Mauern Jerusalems. Die Zeile über zerbrochene Herzen steht neben einer über Sterne."),
"pro-4-23": dict(
 es="De las instrucciones de un padre a su hijo. La palabra hebrea para corazón no habla de sentimientos, sino del lugar donde uno decide y elige.",
 fr="Des instructions d’un père à son fils. Le mot hébreu pour cœur ne concerne pas les sentiments, mais le lieu où l’on décide et choisit.",
 de="Aus den Anweisungen eines Vaters an seinen Sohn. Das hebräische Wort für Herz meint nicht Gefühle, sondern den Ort, an dem ein Mensch entscheidet."),
"pro-16-9": dict(
 es="De una colección de dichos de corte. Los proverbios son observaciones comprimidas, no promesas: la línea describe lo que suele ocurrir, no garantiza un resultado.",
 fr="D’un recueil de sentences de cour. Les proverbes sont des observations condensées, non des promesses : la ligne décrit ce qui arrive d’ordinaire, sans garantir.",
 de="Aus einer Sammlung höfischer Sprüche. Sprichwörter sind verdichtete Beobachtungen, keine Zusagen: die Zeile beschreibt den Regelfall, sie garantiert kein Ergebnis."),
"pro-17-22": dict(
 es="De una colección de observaciones breves sobre la vida diaria. No hay aquí afirmación médica alguna; es sabiduría popular recogida en una compilación.",
 fr="D’un recueil de courtes observations sur la vie quotidienne. Il n’y a ici aucune affirmation médicale ; c’est une sagesse populaire mise par écrit.",
 de="Aus einer Sammlung kurzer Beobachtungen über den Alltag. Es steht hier keine medizinische Aussage; es ist aufgeschriebene Volksweisheit."),
"pro-18-10": dict(
 es="La imagen viene de la vida urbana de entonces: la torre dentro de las murallas era el último sitio al que se replegaban cuando la ciudad ya había caído.",
 fr="L’image vient de la vie urbaine de l’époque : la tour à l’intérieur des remparts était le dernier refuge quand la ville était déjà prise.",
 de="Das Bild stammt aus dem Stadtleben jener Zeit: der Turm innerhalb der Mauern war der letzte Rückzugsort, wenn die Stadt schon gefallen war."),
"ecc-3-1": dict(
 es="De un libro cuyo autor probó riqueza, trabajo y placer y lo llamó todo vapor. La lista de tiempos viene justo después de esa conclusión.",
 fr="D’un livre dont l’auteur a essayé richesse, travail et plaisir et a tout appelé vapeur. La liste des temps vient juste après cette conclusion.",
 de="Aus einem Buch, dessen Verfasser Reichtum, Arbeit und Genuss ausprobierte und alles Windhauch nannte. Die Liste der Zeiten folgt unmittelbar auf diesen Schluss."),
"ecc-4-9": dict(
 es="Observación de un libro que acaba de describir a un hombre que trabaja sin descanso y no tiene hijo, ni hermano, ni nadie por quien trabajar.",
 fr="Observation d’un livre qui vient de décrire un homme travaillant sans répit, sans fils, sans frère et sans personne pour qui travailler.",
 de="Eine Beobachtung aus einem Buch, das eben einen Mann beschrieb, der ohne Pause arbeitet und weder Sohn noch Bruder noch jemanden hat, für den er arbeitet."),
"isa-6-8": dict(
 es="Isaías ve esto el año en que murió el rey Ozías, en el momento en que el país perdió a un gobernante que había reinado cincuenta y dos años.",
 fr="Ésaïe voit cela l’année de la mort du roi Ozias, au moment où le pays perd un souverain qui avait régné cinquante-deux ans.",
 de="Jesaja sieht das im Todesjahr des Königs Usija, in dem Augenblick, als das Land einen Herrscher verlor, der zweiundfünfzig Jahre regiert hatte."),
"isa-26-3": dict(
 es="Línea de un canto que, en el texto del profeta, se cantará cuando todo haya terminado. Está escrita por adelantado, antes de que acabe el desastre.",
 fr="Ligne d’un chant qui, dans le texte du prophète, sera chanté quand tout sera fini. Elle est écrite d’avance, avant la fin du désastre.",
 de="Eine Zeile aus einem Lied, das im Text des Propheten gesungen wird, wenn alles vorbei ist. Sie ist im Voraus geschrieben, noch vor dem Ende der Katastrophe."),
"isa-30-21": dict(
 es="Dicho a un pueblo a punto de resolver sus problemas con una alianza con Egipto sin preguntar a nadie. La voz se promete por detrás, no por delante.",
 fr="Dit à un peuple sur le point de régler ses problèmes par une alliance avec l’Égypte sans consulter personne. La voix est promise derrière, non devant.",
 de="Gesagt zu einem Volk, das seine Probleme durch ein Bündnis mit Ägypten lösen will, ohne jemanden zu fragen. Die Stimme wird von hinten verheißen, nicht von vorn."),
"isa-53-5": dict(
 es="Del canto del siervo sufriente, escrito siglos antes de los hechos del Evangelio y leído por los cristianos como profecía de la crucifixión.",
 fr="Du chant du serviteur souffrant, écrit des siècles avant les faits de l’Évangile et lu par les chrétiens comme une prophétie de la crucifixion.",
 de="Aus dem Lied vom leidenden Knecht, Jahrhunderte vor den Ereignissen der Evangelien geschrieben und von Christen als Weissagung der Kreuzigung gelesen."),
"isa-55-8": dict(
 es="Dicho a gente cuyo regreso no ocurría del modo ni en el tiempo que esperaban. Responde a su desconcierto, no enuncia una idea general.",
 fr="Dit à des gens dont le retour ne se produisait ni comme ni quand ils l’attendaient. Cela répond à leur désarroi, ce n’est pas une idée générale.",
 de="Gesagt zu Menschen, deren Rückkehr nicht so und nicht dann geschah, wie sie erwartet hatten. Es antwortet auf ihre Ratlosigkeit, statt allgemein zu belehren."),
"isa-61-1": dict(
 es="Jesús leyó este pasaje en voz alta en la sinagoga de Nazaret, cerró el rollo y dijo que ese día se había cumplido. Así empezó su ministerio.",
 fr="Jésus lut ce passage à voix haute dans la synagogue de Nazareth, ferma le rouleau et dit qu’il était accompli ce jour-là. Ainsi commença son ministère.",
 de="Jesus las diesen Abschnitt in der Synagoge von Nazareth vor, schloss die Rolle und sagte, er sei an diesem Tag erfüllt. So begann sein Wirken."),
"jer-17-7": dict(
 es="La imagen se entiende en un país con un solo río: un árbol junto al agua sobrevive a la sequía que mata todo lo que crece lejos de ella.",
 fr="L’image prend sens dans un pays à une seule rivière : un arbre près de l’eau survit à la sécheresse qui tue tout ce qui pousse loin d’elle.",
 de="Das Bild ergibt in einem Land mit einem einzigen Fluss Sinn: ein Baum am Wasser überlebt die Dürre, die alles tötet, was fern davon wächst."),
"jer-31-3": dict(
 es="Dicho a un pueblo que acababa de perder su templo, su rey y su tierra. La promesa se da a quienes creían haber sido abandonados para siempre.",
 fr="Dit à un peuple qui venait de perdre son temple, son roi et sa terre. La promesse est faite à ceux qui se croyaient abandonnés pour de bon.",
 de="Gesagt zu einem Volk, das eben Tempel, König und Land verloren hatte. Die Zusage gilt denen, die sich endgültig verlassen glaubten."),
"ezk-36-26": dict(
 es="Ezequiel profetiza en el destierro babilónico, entre los deportados. No habla de mejora personal, sino de lo que ocurrirá a todo un pueblo.",
 fr="Ézéchiel prophétise dans l’exil babylonien, parmi les déportés. Il ne parle pas d’amélioration personnelle, mais de ce qui arrivera à tout un peuple.",
 de="Ezechiel weissagt im babylonischen Exil, unter den Deportierten. Er spricht nicht von persönlicher Besserung, sondern davon, was einem ganzen Volk geschehen wird."),
"dan-3-17": dict(
 es="Tres jóvenes responden al rey que ha ordenado echarlos al horno. Las palabras clave son «y si no»: no saben si Dios los salvará.",
 fr="Trois jeunes gens répondent au roi qui a ordonné de les jeter dans la fournaise. Les mots clés sont « et sinon » : ils ignorent si Dieu les sauvera.",
 de="Drei junge Männer antworten dem König, der befohlen hat, sie in den Ofen zu werfen. Entscheidend ist das „und wenn nicht“: sie wissen nicht, ob Gott rettet."),
"jol-2-25": dict(
 es="Profecía tras una invasión de langosta que destruyó varias cosechas seguidas. La promesa se refiere a años ya vividos en vano.",
 fr="Prophétie après une invasion de sauterelles qui détruisit plusieurs récoltes de suite. La promesse concerne des années déjà vécues en vain.",
 de="Eine Prophetie nach einer Heuschreckenplage, die mehrere Ernten hintereinander vernichtete. Die Zusage betrifft Jahre, die bereits vergeblich gelebt wurden."),
"mic-6-8": dict(
 es="Respuesta a una larga lista de sacrificios que un hombre ofrece traer. El profeta contesta que no es eso lo que se pide, y nombra tres cosas.",
 fr="Réponse à une longue liste de sacrifices qu’un homme propose d’apporter. Le prophète répond que ce n’est pas cela qui est demandé, et nomme trois choses.",
 de="Die Antwort auf eine lange Liste von Opfern, die ein Mensch bringen will. Der Prophet erwidert, das sei nicht gefordert, und nennt stattdessen drei Dinge."),
"hab-3-17": dict(
 es="Final de un libro que empezó con la pregunta «¿hasta cuándo?». El profeta enumera la pérdida total de la cosecha y del ganado, y termina cantando.",
 fr="Fin d’un livre qui commençait par la question « jusqu’à quand ? ». Le prophète énumère la perte totale des récoltes et du bétail, et finit en chantant.",
 de="Das Ende eines Buches, das mit der Frage „wie lange noch?“ begann. Der Prophet zählt Totalausfall der Ernte und totes Vieh auf — und endet mit einem Lied."),
"zep-3-17": dict(
 es="Líneas finales de un libro hecho casi solo de advertencias. Aquí es Dios quien se alegra, no el pueblo, lo cual es un giro poco frecuente.",
 fr="Lignes finales d’un livre fait presque uniquement d’avertissements. Ici, c’est Dieu qui se réjouit, non le peuple : une tournure rare.",
 de="Die Schlusszeilen eines Buches, das fast nur aus Warnungen besteht. Hier freut sich Gott, nicht das Volk — eine seltene Wendung."),
"mat-5-14": dict(
 es="Del Sermón del Monte. Dicho no a una élite, sino a la misma multitud de pobres que minutos antes había oído hablar de los pobres de espíritu.",
 fr="Du Sermon sur la montagne. Dit non à une élite, mais à la même foule de pauvres qui venait d’entendre parler des pauvres en esprit.",
 de="Aus der Bergpredigt. Nicht zu einer Elite gesagt, sondern zu derselben Menge armer Leute, die Minuten zuvor von den Armen im Geiste gehört hatte."),
"mat-6-9": dict(
 es="Jesús da esta oración como modelo, argumentando contra las oraciones públicas largas. Es breve exactamente por esa razón.",
 fr="Jésus donne cette prière comme modèle, en argumentant contre les longues prières publiques. Elle est brève précisément pour cette raison.",
 de="Jesus gibt dieses Gebet als Muster, im Widerspruch zu langen öffentlichen Gebeten. Genau darum ist es kurz."),
"mat-7-7": dict(
 es="Del Sermón del Monte. Lo que sigue es un ejemplo doméstico: un padre que no le dará a su hijo una piedra en lugar de pan.",
 fr="Du Sermon sur la montagne. Ce qui suit est un exemple domestique : un père qui ne tendra pas une pierre à son fils au lieu du pain.",
 de="Aus der Bergpredigt. Was folgt, ist ein häusliches Beispiel: ein Vater, der seinem Sohn keinen Stein statt Brot reicht."),
"mat-18-20": dict(
 es="Dicho en una conversación sobre las peleas dentro de una comunidad y cómo resolverlas. El tema es la reconciliación, no el tamaño de la reunión.",
 fr="Dit dans un entretien sur les querelles au sein d’une communauté et la façon de les régler. Le sujet est la réconciliation, non la taille du rassemblement.",
 de="Gesagt in einem Gespräch über Streit innerhalb einer Gemeinschaft und wie man ihn beilegt. Es geht um Versöhnung, nicht um die Größe der Versammlung."),
"mat-22-37": dict(
 es="Respuesta a un doctor de la ley que vino a ponerlo a prueba. Jesús une en uno solo dos mandamientos de libros distintos.",
 fr="Réponse à un docteur de la loi venu le mettre à l’épreuve. Jésus réunit en un seul deux commandements tirés de livres différents.",
 de="Die Antwort an einen Gesetzeslehrer, der ihn auf die Probe stellen wollte. Jesus fügt zwei Gebote aus verschiedenen Büchern zu einem zusammen."),
"mat-28-20": dict(
 es="Últimas palabras del Evangelio de Mateo, dichas en un monte de Galilea. Dos líneas antes se dice que algunos de los discípulos dudaban.",
 fr="Derniers mots de l’Évangile de Matthieu, prononcés sur une montagne de Galilée. Deux lignes plus haut, il est dit que certains disciples doutaient.",
 de="Die letzten Worte des Matthäusevangeliums, gesprochen auf einem Berg in Galiläa. Zwei Zeilen zuvor heißt es, dass einige der Jünger zweifelten."),
"mrk-10-27": dict(
 es="Respuesta a unos discípulos aturdidos tras la conversación con el joven rico, que preguntaron entonces quién podría salvarse.",
 fr="Réponse à des disciples abasourdis après l’entretien avec le jeune homme riche, qui demandèrent alors qui pouvait être sauvé.",
 de="Die Antwort an Jünger, die nach dem Gespräch mit dem reichen jungen Mann fassungslos fragten, wer denn dann gerettet werden könne."),
"luk-1-37": dict(
 es="Lo dice el ángel a María en una conversación sobre su parienta anciana Isabel, que espera un hijo. Es un argumento, no un consuelo general.",
 fr="Dit par l’ange à Marie dans un entretien sur sa parente âgée Élisabeth, qui attend un enfant. C’est un argument, non une consolation générale.",
 de="Vom Engel zu Maria gesagt, in einem Gespräch über ihre alte Verwandte Elisabet, die ein Kind erwartet. Es ist ein Argument, kein allgemeiner Trost."),
"luk-6-37": dict(
 es="Del Sermón del Llano, la versión de Lucas del Sermón del Monte. Es más corto y se dirige directamente a los oyentes.",
 fr="Du Sermon dans la plaine, version lucanienne du Sermon sur la montagne. Il est plus court et s’adresse directement aux auditeurs.",
 de="Aus der Feldrede, der lukanischen Fassung der Bergpredigt. Sie ist kürzer und wendet sich unmittelbar an die Zuhörer."),

# ── партия 2 ──────────────────────────────────────────────────────────────
"luk-10-41": dict(
 es="Dicho a Marta, que ha acogido a los invitados y prepara sola la comida mientras su hermana está sentada escuchando. Se ha quejado en voz alta.",
 fr="Dit à Marthe, qui a accueilli les hôtes et prépare seule le repas pendant que sa sœur reste assise à écouter. Elle s’est plainte à voix haute.",
 de="Gesagt zu Marta, die Gäste aufgenommen hat und das Essen allein bewältigt, während ihre Schwester dasitzt und zuhört. Sie hat sich laut beschwert."),
"luk-12-7": dict(
 es="El argumento se apoya en lo barato: los gorriones eran la comida más pobre que había, cinco pájaros por dos monedas.",
 fr="L’argument repose sur le bon marché : les moineaux étaient la nourriture la plus pauvre qui soit, cinq oiseaux pour deux pièces.",
 de="Das Argument stützt sich auf den Preis: Sperlinge waren die billigste Nahrung der Ärmsten, fünf Vögel für zwei Münzen."),
"luk-15-20": dict(
 es="De la parábola del hijo pródigo. El padre corre a su encuentro, algo indigno para un hombre mayor de aquel tiempo, y los oyentes lo sabían.",
 fr="De la parabole du fils prodigue. Le père court à sa rencontre, ce qui était indigne pour un homme âgé de l’époque, et les auditeurs le savaient.",
 de="Aus dem Gleichnis vom verlorenen Sohn. Der Vater läuft ihm entgegen — für einen älteren Mann jener Zeit unwürdig, und die Zuhörer wussten das."),
"luk-23-34": dict(
 es="Dicho desde la cruz, sobre quienes en ese momento se reparten su ropa. Es la primera de las siete palabras pronunciadas en la crucifixión.",
 fr="Dit depuis la croix, à propos de ceux qui se partagent ses vêtements à cet instant. C’est la première des sept paroles de la crucifixion.",
 de="Vom Kreuz herab gesagt, über die Leute, die in diesem Moment seine Kleider verteilen. Es ist das erste der sieben Worte bei der Kreuzigung."),
"jhn-1-5": dict(
 es="Del prólogo del Evangelio, escrito como himno. El verbo puede significar «no comprendieron» y «no vencieron»; los traductores deben elegir uno.",
 fr="Du prologue de l’Évangile, écrit comme une hymne. Le verbe peut signifier « n’ont pas compris » et « n’ont pas vaincu » ; il faut choisir.",
 de="Aus dem Prolog des Evangeliums, als Hymnus geschrieben. Das Verb kann „nicht begriffen“ und „nicht überwältigt“ heißen; Übersetzer müssen sich entscheiden."),
"jhn-8-12": dict(
 es="Dicho en el atrio del templo durante la fiesta de las cabañas, cuando allí ardían lámparas enormes toda la semana. La imagen estaba a la vista.",
 fr="Dit dans le parvis du temple pendant la fête des tentes, quand d’immenses lampes y brûlaient toute la semaine. L’image était sous les yeux.",
 de="Gesagt im Tempelvorhof während des Laubhüttenfestes, als dort eine Woche lang riesige Leuchter brannten. Das Bild stand den Zuhörern vor Augen."),
"jhn-10-10": dict(
 es="Del discurso sobre el pastor y el asalariado, dicho después de que a un ciego curado lo expulsaran de la sinagoga por no retractarse.",
 fr="Du discours sur le berger et le mercenaire, dit après qu’un aveugle guéri eut été chassé de la synagogue pour avoir refusé de se rétracter.",
 de="Aus der Rede über den Hirten und den Mietling, gesagt, nachdem ein geheilter Blinder aus der Synagoge geworfen wurde, weil er nicht widerrief."),
"jhn-11-35": dict(
 es="El versículo más corto de los Evangelios. Jesús llora ante la tumba de Lázaro sabiendo que en minutos lo llamará vivo.",
 fr="Le verset le plus court des Évangiles. Jésus pleure devant le tombeau de Lazare en sachant que dans quelques minutes il l’appellera vivant.",
 de="Der kürzeste Vers der Evangelien. Jesus weint am Grab des Lazarus, obwohl er weiß, dass er ihn Minuten später lebend herausrufen wird."),
"jhn-13-34": dict(
 es="Dicho en la mesa, justo después de lavar los pies a los discípulos, tarea que en una casa hacía el esclavo de menor rango.",
 fr="Dit à table, juste après avoir lavé les pieds des disciples, tâche qu’accomplissait dans une maison l’esclave le plus bas.",
 de="Gesagt bei Tisch, direkt nachdem er den Jüngern die Füße gewaschen hatte — eine Arbeit, die im Haus der niedrigste Sklave verrichtete."),
"jhn-15-13": dict(
 es="Dicho la noche antes del arresto, camino del cenáculo. En pocas horas las palabras se vuelven descripción de lo que le ocurre.",
 fr="Dit la nuit avant l’arrestation, en chemin depuis la chambre haute. En quelques heures, ces mots deviennent la description de ce qui lui arrive.",
 de="Gesagt in der Nacht vor der Verhaftung, auf dem Weg vom Obergemach. Wenige Stunden später beschreiben die Worte, was ihm selbst geschieht."),
"jhn-16-33": dict(
 es="Última línea del discurso de despedida, antes de la oración y del camino al huerto donde lo arrestan. La aflicción se promete sin suavizarla.",
 fr="Dernière ligne du discours d’adieu, avant la prière et la marche vers le jardin où il est arrêté. La détresse est annoncée sans être adoucie.",
 de="Die letzte Zeile der Abschiedsrede, vor dem Gebet und dem Gang in den Garten, wo er verhaftet wird. Die Bedrängnis wird ungeschönt zugesagt."),
"act-20-35": dict(
 es="Pablo se despide de los ancianos de Éfeso sabiendo que no volverá a verlos. Cita un dicho de Jesús que no aparece en ningún Evangelio.",
 fr="Paul fait ses adieux aux anciens d’Éphèse en sachant qu’il ne les reverra plus. Il cite une parole de Jésus qu’aucun Évangile ne rapporte.",
 de="Paulus verabschiedet sich von den Ältesten in Ephesus, im Wissen, sie nicht wiederzusehen. Er zitiert ein Jesuswort, das in keinem Evangelium steht."),
"rom-5-8": dict(
 es="Pablo construye el argumento al revés: acaba de observar que casi nadie moriría ni siquiera por un hombre bueno.",
 fr="Paul construit l’argument à rebours : il vient d’observer que presque personne ne mourrait même pour un homme de bien.",
 de="Paulus baut das Argument von hinten auf: er hat eben festgestellt, dass kaum jemand auch nur für einen guten Menschen sterben würde."),
"rom-12-2": dict(
 es="Comienzo de la mitad práctica de la carta, tras once capítulos de argumentación. A partir de aquí Pablo pasa a qué hacer.",
 fr="Début de la moitié pratique de la lettre, après onze chapitres d’argumentation. À partir d’ici, Paul passe à ce qu’il faut faire.",
 de="Der Beginn des praktischen Teils des Briefes, nach elf Kapiteln Argumentation. Von hier an geht Paulus dazu über, was zu tun ist."),
"rom-12-12": dict(
 es="De una lista de instrucciones breves que van una tras otra sin nexos. La aflicción aparece en ella como un hecho dado, no como una posibilidad.",
 fr="D’une liste d’instructions brèves qui se suivent sans liaison. La détresse y figure comme un fait acquis, non comme une éventualité.",
 de="Aus einer Liste kurzer Anweisungen, die ohne Bindewörter aufeinanderfolgen. Die Bedrängnis steht darin als Tatsache, nicht als Möglichkeit."),
"rom-15-13": dict(
 es="Bendición al final de una carta a una comunidad donde judíos y gentiles no lograban ponerse de acuerdo sobre comidas y fiestas.",
 fr="Bénédiction à la fin d’une lettre à une communauté où Juifs et païens ne s’accordaient ni sur la nourriture ni sur les fêtes.",
 de="Ein Segen am Ende eines Briefes an eine Gemeinde, in der Juden und Heiden sich über Speisen und Feste nicht einigen konnten."),
"1co-10-13": dict(
 es="Dicho a corintios que se creían espiritualmente avanzados. Justo antes, Pablo les recordó cómo murieron en el desierto los que estaban muy seguros.",
 fr="Dit à des Corinthiens qui se croyaient spirituellement avancés. Juste avant, Paul leur a rappelé comment les trop sûrs d’eux moururent au désert.",
 de="Gesagt zu Korinthern, die sich für geistlich fortgeschritten hielten. Kurz davor erinnerte Paulus daran, wie die Selbstsicheren in der Wüste starben."),
"1co-13-4": dict(
 es="Escrito no para bodas, sino en medio del arreglo de peleas en una comunidad dividida en bandos que discutían de quién era el don más importante.",
 fr="Écrit non pour les mariages, mais au milieu du règlement de querelles dans une communauté divisée en clans disputant du don le plus important.",
 de="Nicht für Hochzeiten geschrieben, sondern mitten in der Schlichtung von Streit in einer Gemeinde, die stritt, wessen Geistesgabe die wichtigste sei."),
"2co-1-3": dict(
 es="Comienzo de una carta donde Pablo escribirá poco después que en Asia desesperó incluso de la vida. Describe el consuelo como algo que se transmite.",
 fr="Ouverture d’une lettre où Paul écrira bientôt qu’en Asie il désespéra même de la vie. Il décrit la consolation comme quelque chose qui se transmet.",
 de="Der Anfang eines Briefes, in dem Paulus bald schreibt, er habe in Asien selbst am Leben verzweifelt. Trost beschreibt er als etwas Weiterzugebendes."),
"2co-4-16": dict(
 es="Pablo escribe esto tras haber enumerado azotes, naufragios y hambre. La «leve aflicción» es su propia valoración de su propia lista.",
 fr="Paul écrit ceci après avoir énuméré coups, naufrages et faim. La « légère affliction » est sa propre évaluation de sa propre liste.",
 de="Paulus schreibt das, nachdem er Schläge, Schiffbrüche und Hunger aufgezählt hat. Die „leichte Bedrängnis“ ist sein eigenes Urteil über seine eigene Liste."),
"2co-5-17": dict(
 es="De una carta a una comunidad que había conocido a Pablo antes de su conversión, como perseguidor. La afirmación sobre lo nuevo valía primero para él.",
 fr="D’une lettre à une communauté qui avait connu Paul avant sa conversion, comme persécuteur. L’affirmation sur la nouveauté valait d’abord pour lui.",
 de="Aus einem Brief an eine Gemeinde, die Paulus vor seiner Bekehrung als Verfolger kannte. Die Aussage über das Neue galt zuerst ihm selbst."),
"gal-5-22": dict(
 es="La lista viene justo después de un catálogo de las disputas y envidias que ocupaban a la comunidad. Está en singular: un fruto, no nueve.",
 fr="La liste vient juste après un catalogue des querelles et des envies qui occupaient la communauté. Elle est au singulier : un fruit, non neuf.",
 de="Die Liste folgt unmittelbar auf einen Katalog von Streit und Neid, die die Gemeinde beschäftigten. Sie steht im Singular: eine Frucht, nicht neun."),
"eph-2-8": dict(
 es="De una carta a una ciudad famosa por el templo de Artemisa y el comercio de amuletos, donde la religión era un servicio que se pagaba.",
 fr="D’une lettre à une ville célèbre pour le temple d’Artémis et le commerce d’amulettes, où la religion était un service que l’on payait.",
 de="Aus einem Brief an eine Stadt, berühmt für den Artemistempel und den Amuletthandel, wo Religion eine Dienstleistung gegen Bezahlung war."),
"eph-3-20": dict(
 es="Final de la oración con que Pablo cierra la primera mitad de la carta. Después empieza la parte práctica; este es el gozne.",
 fr="Fin de la prière par laquelle Paul clôt la première moitié de la lettre. Ensuite commence la partie pratique ; c’est la charnière.",
 de="Das Ende des Gebets, mit dem Paulus die erste Briefhälfte schließt. Danach beginnt der praktische Teil; hier ist das Scharnier."),
"eph-6-10": dict(
 es="La imagen de la armadura se toma de un soldado romano, visión diaria en el puerto de Éfeso. Pablo la escribió bajo custodia de hombres así.",
 fr="L’image de l’armure vient d’un soldat romain, spectacle quotidien dans le port d’Éphèse. Paul l’a écrite sous la garde de tels hommes.",
 de="Das Bild der Rüstung stammt vom römischen Soldaten, im Hafen von Ephesus täglich zu sehen. Paulus schrieb es in der Bewachung solcher Männer."),
"php-1-6": dict(
 es="Pablo escribe a una comunidad que él mismo fundó y que le envió dinero mientras estaba preso. Es una carta de agradecimiento.",
 fr="Paul écrit à une communauté qu’il a lui-même fondée et qui lui a envoyé de l’argent pendant sa détention. C’est une lettre de remerciement.",
 de="Paulus schreibt an eine Gemeinde, die er selbst gegründet hat und die ihm im Gefängnis Geld schickte. Es ist ein Dankesbrief."),
"php-2-3": dict(
 es="Dicho a una comunidad donde, como muestra el final de la carta, dos mujeres se habían enemistado tanto que Pablo las nombró en público.",
 fr="Dit à une communauté où, comme le montre la fin de la lettre, deux femmes s’étaient brouillées au point que Paul les nomme publiquement.",
 de="Gesagt zu einer Gemeinde, in der sich, wie das Briefende zeigt, zwei Frauen so zerstritten hatten, dass Paulus sie öffentlich beim Namen nannte."),
"php-4-8": dict(
 es="Viene justo después del consejo de no inquietarse. Pablo propone no reprimir los pensamientos sino sustituirlos, y enumera por cuáles.",
 fr="Cela vient juste après le conseil de ne pas s’inquiéter. Paul propose non de réprimer les pensées mais de les remplacer, et dit par quoi.",
 de="Es folgt unmittelbar auf den Rat, sich nicht zu sorgen. Paulus schlägt vor, Gedanken nicht zu unterdrücken, sondern zu ersetzen, und zählt auf womit."),
"col-3-23": dict(
 es="Dicho en una sección sobre deberes domésticos, con las líneas más cercanas dirigidas a esclavos. Los oyentes eran gente sin elección de trabajo.",
 fr="Dit dans une section sur les devoirs domestiques, les lignes les plus proches s’adressant aux esclaves. Les auditeurs n’avaient aucun choix de travail.",
 de="Gesagt in einem Abschnitt über Hausordnung, dessen nächste Zeilen sich an Sklaven richten. Die Zuhörer hatten keine Wahl ihrer Arbeit."),
"1th-4-13": dict(
 es="La comunidad había enterrado a sus primeros muertos y estaba perdida. Pablo no prohíbe el duelo: distingue el duelo con esperanza del duelo sin ella.",
 fr="La communauté venait d’enterrer ses premiers morts et était désemparée. Paul n’interdit pas le deuil : il distingue le deuil avec espérance et sans.",
 de="Die Gemeinde hatte ihre ersten Toten begraben und war ratlos. Paulus verbietet die Trauer nicht; er unterscheidet Trauer mit Hoffnung von Trauer ohne."),
"2ti-1-7": dict(
 es="Última carta de Pablo, escrita esperando la ejecución al joven Timoteo, que quedó al frente de una comunidad y, a juzgar por el texto, tenía miedo.",
 fr="Dernière lettre de Paul, écrite dans l’attente de l’exécution au jeune Timothée, laissé à la tête d’une communauté et, d’après le texte, effrayé.",
 de="Der letzte Brief des Paulus, in Erwartung der Hinrichtung an den jungen Timotheus geschrieben, der eine Gemeinde leiten sollte und offenbar Angst hatte."),
"heb-4-16": dict(
 es="La carta se dirige a gente habituada a un templo donde solo un sacerdote se acercaba al lugar santo, una vez al año. De ahí la palabra «confianza».",
 fr="La lettre s’adresse à des gens habitués à un temple où seul un prêtre approchait du lieu saint, une fois l’an. D’où le mot « assurance ».",
 de="Der Brief richtet sich an Menschen, die einen Tempel kannten, in dem nur ein Priester einmal im Jahr das Heiligtum betrat. Daher das Wort „Zuversicht“."),
"heb-12-1": dict(
 es="Imagen de estadio: los testigos en las gradas son las personas enumeradas en el capítulo anterior, que murieron sin ver lo prometido.",
 fr="Image de stade : les témoins dans les tribunes sont les gens énumérés au chapitre précédent, morts sans avoir vu la promesse.",
 de="Ein Stadionbild: die Zeugen auf den Rängen sind die im vorigen Kapitel aufgezählten Menschen, die starben, ohne das Verheißene zu sehen."),
"heb-13-5": dict(
 es="Cita del último discurso de Moisés, recogida en una carta a gente cuyos bienes, como dice antes el texto, habían sido confiscados por su fe.",
 fr="Citation du dernier discours de Moïse, reprise dans une lettre à des gens dont les biens, dit le texte plus haut, furent saisis à cause de leur foi.",
 de="Ein Zitat aus der letzten Rede des Mose, in einem Brief an Menschen, deren Besitz laut Text zuvor ihres Glaubens wegen beschlagnahmt wurde."),
"jas-1-2": dict(
 es="Carta a cristianos dispersos por el imperio. Santiago no dice que las pruebas sean agradables; dice qué hacer con ellas.",
 fr="Lettre à des chrétiens dispersés dans l’empire. Jacques ne dit pas que les épreuves sont agréables ; il dit quoi en faire.",
 de="Ein Brief an Christen, die über das Reich verstreut waren. Jakobus sagt nicht, Prüfungen seien angenehm; er sagt, was mit ihnen zu tun ist."),
"jas-1-5": dict(
 es="Viene justo después de las palabras sobre las pruebas: la sabiduría que hace falta no es general, sino para entender una situación difícil concreta.",
 fr="Cela vient juste après les mots sur les épreuves : la sagesse nécessaire n’est pas générale, mais pour comprendre une situation difficile précise.",
 de="Es folgt direkt auf die Worte über Prüfungen: die nötige Weisheit ist keine allgemeine, sondern die für eine bestimmte schwere Lage."),
"jas-5-16": dict(
 es="Dicho a una comunidad donde, a juzgar por la carta, adular a los ricos y despreciar a los pobres era normal. La confesión se propone como mutua.",
 fr="Dit à une communauté où, à en juger par la lettre, flatter les riches et mépriser les pauvres était courant. L’aveu est proposé comme mutuel.",
 de="Gesagt zu einer Gemeinde, in der es dem Brief nach üblich war, Reiche zu hofieren und Arme zu verachten. Das Bekennen wird als gegenseitig vorgeschlagen."),
"1pe-4-10": dict(
 es="Pedro escribe a cristianos a quienes sus vecinos trataban como extraños. El consejo de servirse unos a otros se da a una comunidad sin apoyo externo.",
 fr="Pierre écrit à des chrétiens que leurs voisins traitaient en étrangers. Le conseil de se servir mutuellement s’adresse à une communauté sans appui extérieur.",
 de="Petrus schreibt an Christen, die ihre Nachbarn als Fremde behandelten. Der Rat, einander zu dienen, gilt einer Gemeinde ohne Rückhalt von außen."),
"1jn-1-9": dict(
 es="Carta a una comunidad donde algunos afirmaban no tener pecado alguno. Es una objeción a ellos, no una regla general.",
 fr="Lettre à une communauté où certains prétendaient n’avoir aucun péché. C’est une objection à leur adresse, non une règle générale.",
 de="Ein Brief an eine Gemeinde, in der einige behaupteten, überhaupt keine Sünde zu haben. Es ist ein Einwand gegen sie, keine allgemeine Regel."),
"1jn-4-18": dict(
 es="El miedo del que se habla es el miedo al castigo, como dice la propia línea. No es una promesa de intrepidez en general.",
 fr="La peur dont il s’agit est la peur du châtiment, comme le dit la ligne elle-même. Ce n’est pas une promesse d’intrépidité en général.",
 de="Die gemeinte Furcht ist die Furcht vor Strafe, wie die Zeile selbst sagt. Es ist keine Zusage allgemeiner Angstfreiheit."),
"rev-3-20": dict(
 es="Dicho a la iglesia de Laodicea, ciudad rica con agua mala traída por acueducto que llegaba tibia. De ahí la imagen.",
 fr="Dit à l’Église de Laodicée, ville riche dont l’eau, amenée par aqueduc, arrivait tiède. D’où l’image.",
 de="Gesagt an die Gemeinde in Laodizea, einer reichen Stadt, deren Wasser über eine Leitung kam und lauwarm ankam. Daher das Bild."),
"gen-2-18": dict(
 es="Lo primero que la Biblia llama no bueno no es el pecado, sino estar solo. Dicho antes de que nada se rompiera, cuando todo lo demás era bueno.",
 fr="La première chose que la Bible dit non bonne n’est pas le péché mais la solitude. Dit avant toute rupture, quand tout le reste avait été dit bon.",
 de="Das Erste, was die Bibel nicht gut nennt, ist nicht die Sünde, sondern das Alleinsein. Gesagt, bevor etwas zerbrach, als alles andere gut hieß."),
"gen-3-9": dict(
 es="La primera pregunta que Dios hace a un ser humano en la Biblia. Adán ya se ha escondido, y la pregunta suena menos a búsqueda que a llamada.",
 fr="La première question que Dieu pose à un être humain dans la Bible. Adam s’est déjà caché, et la question sonne moins comme une recherche qu’un appel.",
 de="Die erste Frage, die Gott in der Bibel an einen Menschen richtet. Adam hat sich schon versteckt, und die Frage klingt weniger nach Suche als nach Ruf."),
"gen-12-1": dict(
 es="Abram tiene setenta y cinco años y se le manda dejar la ciudad donde vivió toda su vida, sin decirle adónde. Sabrá el destino en el camino.",
 fr="Abram a soixante-quinze ans et reçoit l’ordre de quitter la ville où il a toujours vécu, sans qu’on lui dise où aller. Il l’apprendra en chemin.",
 de="Abram ist fünfundsiebzig und soll die Stadt verlassen, in der er sein Leben lang wohnte, ohne zu erfahren, wohin. Das Ziel erfährt er unterwegs."),
"gen-15-5": dict(
 es="Abram ya es viejo y sin hijos, y acaba de decirlo en voz alta. Lo sacan fuera de noche y le mandan contar las estrellas.",
 fr="Abram est déjà vieux et sans enfant, et il vient de le dire à voix haute. On le fait sortir la nuit et on lui dit de compter les étoiles.",
 de="Abram ist schon alt und kinderlos und hat es eben laut gesagt. Man führt ihn nachts hinaus und heißt ihn die Sterne zählen."),
"gen-16-13": dict(
 es="Son palabras de Agar, esclava embarazada que ha huido al desierto de su señora. Es la primera persona en la Biblia que da un nombre a Dios.",
 fr="Ce sont les mots d’Agar, esclave enceinte enfuie au désert loin de sa maîtresse. Elle est la première personne de la Bible à donner un nom à Dieu.",
 de="Es sind die Worte Hagars, einer schwangeren Sklavin, die vor ihrer Herrin in die Wüste floh. Sie ist die Erste in der Bibel, die Gott einen Namen gibt."),
"gen-32-26": dict(
 es="Jacob lucha toda la noche en un vado, la víspera de encontrarse con el hermano al que engañó veinte años antes. Saldrá de esa noche cojeando.",
 fr="Jacob lutte toute la nuit à un gué, la veille de retrouver le frère qu’il a trompé vingt ans plus tôt. Il sortira de cette nuit en boitant.",
 de="Jakob ringt die Nacht hindurch an einer Furt, am Vorabend der Begegnung mit dem Bruder, den er vor zwanzig Jahren betrog. Er geht hinkend daraus hervor."),
"gen-39-2": dict(
 es="Dicho de José en el período en que era esclavo en tierra extranjera, vendido por sus propios hermanos. La palabra «éxito» aparece justo aquí.",
 fr="Dit de Joseph à l’époque où il était esclave en pays étranger, vendu par ses propres frères. Le mot « réussite » apparaît précisément ici.",
 de="Gesagt über Josef in der Zeit, als er Sklave in einem fremden Land war, von den eigenen Brüdern verkauft. Genau hier steht das Wort „Gelingen“."),
"exo-3-14": dict(
 es="Moisés pregunta qué decir si le piden un nombre. La respuesta se construye sobre el verbo «ser», y cada edición la traduce a su manera.",
 fr="Moïse demande quoi dire si on lui réclame un nom. La réponse est bâtie sur le verbe « être », et chaque édition la rend à sa manière.",
 de="Mose fragt, was er sagen soll, wenn man nach einem Namen fragt. Die Antwort baut auf dem Verb „sein“, und jede Ausgabe gibt sie anders wieder."),
"exo-34-6": dict(
 es="Dicho justo después del becerro de oro, cuando Moisés había tallado tablas nuevas para sustituir las que rompió. Profetas y salmos citarán esta fórmula.",
 fr="Dit juste après le veau d’or, quand Moïse eut taillé de nouvelles tables pour remplacer celles qu’il avait brisées. Prophètes et psaumes citeront cette formule.",
 de="Gesagt direkt nach dem Goldenen Kalb, als Mose neue Tafeln behauen hatte für die zerbrochenen. Propheten und Psalmen zitieren diese Formel später."),
"lev-19-18": dict(
 es="Línea de un código de reglas cotidianas sobre cosechas, pesos y tribunales. Jesús la llamará después el segundo mandamiento, sacándola de esa lista.",
 fr="Ligne d’un code de règles quotidiennes sur les récoltes, les poids et les tribunaux. Jésus l’appellera plus tard le second commandement, hors de cette liste.",
 de="Eine Zeile aus einem Kodex alltäglicher Regeln über Ernten, Gewichte und Gerichte. Jesus nennt sie später das zweite Gebot und hebt sie heraus."),
"num-23-19": dict(
 es="Lo dice Balaam, un adivino contratado para maldecir a Israel. Lo intenta tres veces y tres veces pronuncia una bendición en su lugar.",
 fr="Dit par Balaam, un devin engagé pour maudire Israël. Il essaie trois fois et trois fois prononce une bénédiction à la place.",
 de="Gesprochen von Bileam, einem Wahrsager, der Israel verfluchen sollte. Dreimal versucht er es und spricht dreimal stattdessen einen Segen."),
"deu-8-3": dict(
 es="Moisés explica para qué fueron los cuarenta años del desierto. Jesús citará esta misma línea al responder a la primera tentación, también hambriento.",
 fr="Moïse explique à quoi ont servi les quarante ans du désert. Jésus citera cette même ligne pour répondre à la première tentation, affamé lui aussi.",
 de="Mose erklärt, wozu die vierzig Wüstenjahre dienten. Jesus zitiert dieselbe Zeile bei der ersten Versuchung — ebenfalls in der Wüste, ebenfalls hungrig."),
"deu-30-19": dict(
 es="Moisés pone una elección ante el pueblo en su último discurso y llama por testigos al cielo y a la tierra: fórmula jurídica de tratado de la época.",
 fr="Moïse place un choix devant le peuple dans son dernier discours et prend à témoin le ciel et la terre : formule juridique de traité de l’époque.",
 de="Mose stellt dem Volk in seiner letzten Rede eine Wahl und ruft Himmel und Erde als Zeugen an — eine juristische Vertragsformel jener Zeit."),
"deu-31-8": dict(
 es="Dicho a Josué delante de todo el pueblo. Moisés entrega el mando en público para que todos vean al sucesor, y dice que no irá solo delante.",
 fr="Dit à Josué devant tout le peuple. Moïse transmet le commandement en public pour que chacun voie le successeur, et dit qu’il ne marchera pas seul devant.",
 de="Gesagt zu Josua vor dem ganzen Volk. Mose übergibt die Führung öffentlich, damit alle den Nachfolger sehen — und sagt, er gehe nicht allein voran."),
"jos-1-8": dict(
 es="Dicho a un jefe nuevo en su primer día. El verbo traducido «meditar» significa en hebreo murmurar en voz alta: entonces no se leía en silencio.",
 fr="Dit à un chef nouveau, son premier jour. Le verbe rendu par « méditer » signifie en hébreu marmonner à voix haute : on ne lisait pas en silence.",
 de="Gesagt zu einem neuen Anführer an seinem ersten Tag. Das mit „sinnen“ übersetzte Verb heißt hebräisch halblaut murmeln — man las damals nicht still."),
"jdg-6-12": dict(
 es="Así llaman a Gedeón en el momento en que trilla trigo en un lagar, escondido de los saqueadores. Enseguida objeta que debe de ser un error.",
 fr="Voilà comment Gédéon est appelé au moment où il bat le blé dans un pressoir, caché des pillards. Il objecte aussitôt que ce doit être une erreur.",
 de="So wird Gideon genannt, während er in einer Kelter Weizen drischt, versteckt vor Plünderern. Er wendet sofort ein, das müsse ein Irrtum sein."),
"rut-1-16": dict(
 es="Dicho por Rut, mujer extranjera viuda joven. Se niega a volver a casa y parte con su suegra a un país donde será una forastera.",
 fr="Dit par Ruth, une étrangère veuve jeune. Elle refuse de rentrer chez elle et part avec sa belle-mère vers un pays où elle sera étrangère.",
 de="Gesprochen von Rut, einer jung verwitweten Ausländerin. Sie weigert sich heimzukehren und zieht mit ihrer Schwiegermutter in ein Land, wo sie fremd sein wird."),
"1sa-3-10": dict(
 es="Samuel tiene aquí unos doce años y tres veces ha confundido la voz con la del sacerdote anciano. Fue el sacerdote quien le enseñó esta respuesta.",
 fr="Samuel a ici une douzaine d’années et a trois fois pris la voix pour celle du vieux prêtre. C’est le prêtre qui lui a appris cette réponse.",
 de="Samuel ist hier etwa zwölf und hat die Stimme dreimal für die des alten Priesters gehalten. Der Priester war es, der ihm diese Antwort beibrachte."),
"1sa-17-47": dict(
 es="Dicho por un adolescente sin armadura a un hombre armado por completo, ante dos ejércitos que llevaban cuarenta días frente a frente sin moverse.",
 fr="Dit par un adolescent sans armure à un homme entièrement armé, devant deux armées qui se faisaient face depuis quarante jours sans bouger.",
 de="Gesprochen von einem Jungen ohne Rüstung zu einem voll bewaffneten Mann, vor zwei Heeren, die sich vierzig Tage lang bewegungslos gegenüberstanden."),
"1sa-30-6": dict(
 es="La ciudad de David está quemada, las familias de sus hombres se las han llevado y sus propios soldados hablan de apedrearlo. No hay ayuda de nadie.",
 fr="La ville de David est brûlée, les familles de ses hommes emmenées, et ses propres soldats parlent de le lapider. Il n’a d’aide de personne.",
 de="Davids Stadt ist verbrannt, die Familien seiner Männer verschleppt, und seine eigenen Soldaten reden davon, ihn zu steinigen. Von niemandem kommt Hilfe."),
"1ki-18-21": dict(
 es="Elías se dirige al pueblo en el monte Carmelo, donde todos se han reunido. El texto dice que no le respondieron ni una palabra.",
 fr="Élie s’adresse au peuple sur le mont Carmel, où tous se sont rassemblés. Le texte dit qu’ils ne lui répondirent pas un mot.",
 de="Elia wendet sich auf dem Karmel an das Volk, wo alle versammelt sind. Der Text sagt, sie antworteten ihm kein Wort."),
"2ki-6-16": dict(
 es="La ciudad está rodeada por un ejército y el criado del profeta entra en pánico. Eliseo pide que se le abran los ojos, y ve lo que un minuto antes no.",
 fr="La ville est cernée par une armée et le serviteur du prophète panique. Élisée demande qu’on lui ouvre les yeux, et il voit ce qu’il ne voyait pas.",
 de="Die Stadt ist von einem Heer umzingelt, und der Diener des Propheten gerät in Panik. Elischa bittet, ihm die Augen zu öffnen — und er sieht."),
"1ch-16-11": dict(
 es="Del canto entonado el día en que el arca entró por fin en Jerusalén, tras una pausa de tres meses causada por un accidente mortal en el camino.",
 fr="Du chant entonné le jour où l’arche entra enfin à Jérusalem, après une pause de trois mois causée par un accident mortel en chemin.",
 de="Aus dem Lied, das an dem Tag gesungen wurde, als die Lade endlich nach Jerusalem kam — nach drei Monaten Pause wegen eines tödlichen Unfalls unterwegs."),
"2ch-7-14": dict(
 es="Dicho a Salomón de noche tras la dedicación del templo. La promesa es condicional y va dirigida a un pueblo concreto en una tierra concreta.",
 fr="Dit à Salomon la nuit après la dédicace du temple. La promesse est conditionnelle et s’adresse à un peuple précis dans un pays précis.",
 de="Gesagt zu Salomo in der Nacht nach der Tempelweihe. Die Zusage ist an Bedingungen geknüpft und gilt einem bestimmten Volk in einem bestimmten Land."),
"ezr-3-12": dict(
 es="Se pone el cimiento del segundo templo. Los jóvenes gritan de alegría, los viejos lloran porque recuerdan el primero, y los dos sonidos no se distinguían.",
 fr="On pose les fondations du second temple. Les jeunes crient de joie, les vieux pleurent car ils se souviennent du premier, et l’on ne distinguait pas les deux.",
 de="Der Grundstein des zweiten Tempels wird gelegt. Die Jungen jubeln, die Alten weinen, weil sie den ersten kannten — und beides war nicht zu unterscheiden."),
"neh-6-3": dict(
 es="Respuesta a los adversarios que invitaron cuatro veces a Nehemías a negociar para apartarlo de la obra. Da la misma respuesta las cuatro veces.",
 fr="Réponse aux adversaires qui invitèrent quatre fois Néhémie à des pourparlers pour l’écarter du chantier. Il donne la même réponse les quatre fois.",
 de="Die Antwort an Gegner, die Nehemia viermal zu Verhandlungen einluden, um ihn von der Baustelle wegzulocken. Viermal gibt er dieselbe Antwort."),
"est-4-14": dict(
 es="Mardoqueo escribe esto a Ester, una reina que oculta su origen. Presentarse ante el rey sin ser llamada significaba la muerte, y ella lo sabía.",
 fr="Mardochée écrit ceci à Esther, une reine qui cache son origine. Se présenter au roi sans être appelée signifiait la mort, et elle le savait.",
 de="Mordechai schreibt das an Ester, eine Königin, die ihre Herkunft verbirgt. Ungerufen vor den König zu treten bedeutete den Tod, und sie wusste es."),
"job-1-21": dict(
 es="Job lo dice el día en que llegaron cuatro mensajes seguidos: ganado robado, criados muertos y sus diez hijos aplastados por una casa derrumbada.",
 fr="Job le dit le jour où quatre messages arrivèrent coup sur coup : bétail volé, serviteurs tués, et ses dix enfants écrasés sous une maison effondrée.",
 de="Hiob sagt das an dem Tag, an dem vier Nachrichten nacheinander eintrafen: Vieh geraubt, Knechte erschlagen und alle zehn Kinder unter einem Haus begraben."),
"job-23-10": dict(
 es="Job acaba de decir que busca a Dios y no lo halla ni delante ni detrás. La línea sobre ser conocido viene justo tras admitir que él mismo no ve nada.",
 fr="Job vient de dire qu’il cherche Dieu et ne le trouve ni devant ni derrière. La ligne sur être connu suit l’aveu qu’il ne voit lui-même rien.",
 de="Hiob hat eben gesagt, er suche Gott und finde ihn weder vorn noch hinten. Die Zeile übers Gekanntsein folgt dem Eingeständnis, selbst nichts zu sehen."),
"psa-3-5": dict(
 es="El encabezado sitúa este salmo cuando David huía de su propio hijo, que había levantado una revuelta. Escribe que durmió mientras lo perseguían.",
 fr="Le titre situe ce psaume quand David fuyait son propre fils, qui avait soulevé une révolte. Il écrit qu’il a dormi alors qu’on le traquait.",
 de="Die Überschrift verortet diesen Psalm in der Flucht Davids vor dem eigenen Sohn, der einen Aufstand angezettelt hatte. Er schreibt, er habe geschlafen."),
"psa-8-3": dict(
 es="Salmo de David escrito, a juzgar por el texto, de noche a cielo abierto. La pregunta sobre el hombre se hace ante las estrellas, no en un templo.",
 fr="Psaume de David écrit, à en juger par le texte, la nuit à ciel ouvert. La question sur l’homme est posée face aux étoiles, non dans un temple.",
 de="Ein Psalm Davids, dem Text nach nachts unter freiem Himmel geschrieben. Die Frage nach dem Menschen wird vor den Sternen gestellt, nicht im Tempel."),
"psa-13-1": dict(
 es="El salmo se abre con cuatro preguntas seguidas de «¿hasta cuándo?». Es una queja directa por el silencio, no una reflexión piadosa sobre él.",
 fr="Le psaume s’ouvre sur quatre questions « jusqu’à quand ? » de suite. C’est une plainte directe contre le silence, non une pieuse réflexion.",
 de="Der Psalm beginnt mit vier „Wie lange noch“-Fragen hintereinander. Es ist eine direkte Klage über das Schweigen, keine fromme Betrachtung darüber."),
"psa-20-7": dict(
 es="Salmo que se cantaba antes de que el ejército saliera. Los carros y caballos eran entonces lo que hoy los tanques, e Israel casi no tenía.",
 fr="Psaume chanté avant le départ de l’armée. Les chars et les chevaux étaient alors ce que sont les chars aujourd’hui, et Israël n’en avait presque pas.",
 de="Ein Psalm, den man sang, bevor das Heer auszog. Wagen und Pferde waren damals, was heute Panzer sind — und Israel hatte fast keine."),
"psa-22-1": dict(
 es="Salmo de David que se abre con un grito de abandono. Jesús pronuncia esta línea desde la cruz, y quienes lo oían sabían cómo termina el salmo.",
 fr="Psaume de David qui s’ouvre sur un cri d’abandon. Jésus prononce cette ligne depuis la croix, et ceux qui écoutaient savaient comment le psaume finit.",
 de="Ein Psalm Davids, der mit einem Schrei der Verlassenheit beginnt. Jesus spricht diese Zeile am Kreuz, und die Zuhörer wussten, wie der Psalm endet."),
"psa-25-4": dict(
 es="Acróstico según el alfabeto hebreo: cada línea empieza con la letra siguiente. La petición sobre el camino y la del perdón van juntas, no por separado.",
 fr="Acrostiche sur l’alphabet hébreu : chaque ligne commence par la lettre suivante. La demande sur le chemin et celle du pardon vont ensemble.",
 de="Ein Akrostichon nach dem hebräischen Alphabet: jede Zeile beginnt mit dem nächsten Buchstaben. Die Bitte um den Weg und die um Vergebung stehen nebeneinander."),
"psa-31-15": dict(
 es="Salmo de un hombre que escribe que está olvidado como un muerto y oye cuchicheos alrededor. Las palabras sobre el tiempo se dicen desde ahí.",
 fr="Psaume d’un homme qui écrit qu’il est oublié comme un mort et entend chuchoter autour de lui. Les mots sur le temps sont dits de cette position.",
 de="Der Psalm eines Mannes, der schreibt, er sei vergessen wie ein Toter, und ringsum Getuschel hört. Von dort aus sind die Worte über die Zeit gesagt."),
"psa-34-8": dict(
 es="La invitación se apoya en el gusto, el más corporal de los sentidos. El salmo se escribió después de que David escapara fingiendo estar loco.",
 fr="L’invitation s’appuie sur le goût, le plus corporel des sens. Le psaume fut écrit après que David eut échappé de justesse en feignant la folie.",
 de="Die Einladung stützt sich auf den Geschmack, den leiblichsten der Sinne. Der Psalm entstand, nachdem David knapp entkam, indem er Wahnsinn vortäuschte."),
"psa-40-1": dict(
 es="Salmo de David sobre ser sacado de un pozo de barro. La palabra traducida «con paciencia» significa literalmente «esperó y esperó».",
 fr="Psaume de David sur le fait d’être tiré d’une fosse de boue. Le mot rendu par « avec patience » signifie littéralement « il attendit et attendit ».",
 de="Ein Psalm Davids darüber, aus einer Schlammgrube gezogen zu werden. Das mit „geduldig“ übersetzte Wort heißt wörtlich „er harrte und harrte“."),
"psa-46-10": dict(
 es="La línea está en un salmo donde la tierra se hunde y las lanzas se quiebran. El verbo hebreo se acerca más a «dejad caer las manos» que a «callad».",
 fr="La ligne se trouve dans un psaume où la terre cède et où les lances se brisent. Le verbe hébreu tient plus de « laissez tomber les mains » que de « taisez-vous ».",
 de="Die Zeile steht in einem Psalm, in dem die Erde weicht und Speere zerbrechen. Das hebräische Verb heißt eher „lasst die Hände sinken“ als „seid still“."),
"psa-61-2": dict(
 es="David escribe que llama desde el extremo de la tierra cuando su corazón desfallece. Pide no fuerza, sino que lo suban más alto de lo que él puede.",
 fr="David écrit qu’il appelle du bout de la terre quand son cœur défaille. Il demande non la force, mais d’être élevé plus haut qu’il ne peut monter.",
 de="David schreibt, er rufe vom Ende der Erde, wenn sein Herz verzagt. Er bittet nicht um Kraft, sondern darum, höher gehoben zu werden, als er steigen kann."),
"psa-68-6": dict(
 es="Salmo procesional que se cantaba mientras se llevaba el santuario. La línea sobre huérfanos y solitarios está en una lista de a quién atiende Dios primero.",
 fr="Psaume de procession chanté pendant qu’on portait le sanctuaire. La ligne sur les orphelins et les isolés figure dans une liste de ce dont Dieu s’occupe d’abord.",
 de="Ein Prozessionspsalm, gesungen beim Tragen des Heiligtums. Die Zeile über Waisen und Einsame steht in einer Liste dessen, worum Gott sich zuerst kümmert."),
"psa-71-9": dict(
 es="Salmo de un anciano: escribe que confía en Dios desde su juventud y pide no ser dejado ahora que se le acaban las fuerzas. Es una oración sobre la vejez.",
 fr="Psaume d’un vieillard : il écrit qu’il se fie à Dieu depuis sa jeunesse et demande à ne pas être lâché maintenant que ses forces s’en vont.",
 de="Der Psalm eines alten Mannes: er schreibt, er vertraue Gott seit seiner Jugend, und bittet, jetzt nicht fallen gelassen zu werden, da die Kraft schwindet."),
"psa-77-11": dict(
 es="Salmo de un hombre que no puede dormir y pregunta si Dios ha olvidado tener misericordia. Recurre a recordar el pasado porque el presente no le dice nada.",
 fr="Psaume d’un homme qui ne peut dormir et demande si Dieu a oublié d’avoir pitié. Il se tourne vers le passé parce que le présent ne lui dit rien.",
 de="Der Psalm eines Mannes, der nicht schlafen kann und fragt, ob Gott vergessen hat, gnädig zu sein. Er wendet sich der Erinnerung zu, weil die Gegenwart schweigt."),
"psa-86-11": dict(
 es="Petición de un corazón no dividido: literalmente, dejar de querer cosas opuestas a la vez. El salmo está escrito en peligro de hombres violentos.",
 fr="Demande d’un cœur non partagé : littéralement, cesser de vouloir des choses opposées à la fois. Le psaume est écrit sous la menace d’hommes violents.",
 de="Die Bitte um ein ungeteiltes Herz — wörtlich darum, nicht länger Gegensätzliches zugleich zu wollen. Der Psalm ist in Gefahr durch Gewalttätige geschrieben."),
"psa-88-18": dict(
 es="El único salmo que termina sin alivio: la oscuridad es la última palabra. No llega a ningún consuelo, y así se ha dejado.",
 fr="Le seul psaume qui finit sans soulagement : les ténèbres sont le dernier mot. Il n’arrive à aucune consolation, et on l’a laissé tel quel.",
 de="Der einzige Psalm, der ohne Erleichterung endet: Finsternis ist das letzte Wort. Er kommt bei keinem Trost an, und so hat man ihn stehen lassen."),
"psa-102-17": dict(
 es="El encabezado llama a esto la oración de un afligido que derrama su angustia. El autor escribe que está solo como un pájaro en un tejado.",
 fr="Le titre appelle cela la prière d’un malheureux qui répand sa plainte. L’auteur écrit qu’il est seul comme un oiseau sur un toit.",
 de="Die Überschrift nennt das Gebet eines Elenden, der seine Klage ausschüttet. Der Verfasser schreibt, er sitze allein wie ein Vogel auf dem Dach."),
"psa-112-7": dict(
 es="Acróstico sobre una persona que vive con honradez. La línea no promete que no habrá malas noticias; trata de cómo se reciben.",
 fr="Acrostiche sur une personne qui vit honnêtement. La ligne ne promet pas l’absence de mauvaises nouvelles ; elle parle de la manière de les recevoir.",
 de="Ein Akrostichon über einen Menschen, der redlich lebt. Die Zeile verspricht keine ausbleibenden schlechten Nachrichten; sie handelt davon, wie man sie aufnimmt."),
"psa-113-7": dict(
 es="Salmo del ciclo pascual. La imagen es literal: los pobres de entonces se sentaban en el polvo junto a las puertas y en los basureros de las afueras.",
 fr="Psaume du cycle pascal. L’image est littérale : les pauvres d’alors s’asseyaient dans la poussière près des portes et sur les tas d’ordures hors la ville.",
 de="Ein Psalm aus dem Passazyklus. Das Bild ist wörtlich: die Armen jener Zeit saßen im Staub bei den Toren und auf den Müllhaufen vor der Stadt."),
"psa-118-6": dict(
 es="El último salmo del Hallel pascual, cantado al final de la cena de Pascua. Habla un hombre a quien rodearon por todos lados y salió con vida.",
 fr="Le dernier psaume du Hallel pascal, chanté à la fin du repas de Pâque. Celui qui parle a été cerné de toutes parts et en est sorti vivant.",
 de="Der letzte Psalm des Passa-Hallel, gesungen am Ende des Passamahls. Es spricht ein Mann, den man von allen Seiten umringte und der lebend herauskam."),
"psa-119-71": dict(
 es="Línea del acróstico sobre la ley. El autor habla de su propia desgracia en pasado: la evalúa desde el otro lado.",
 fr="Ligne de l’acrostiche sur la loi. L’auteur parle de son propre malheur au passé : il l’évalue depuis l’autre rive.",
 de="Eine Zeile aus dem Akrostichon über das Gesetz. Der Verfasser spricht von seinem Unglück in der Vergangenheit: er beurteilt es von der anderen Seite."),
"psa-122-1": dict(
 es="Cántico de las subidas sobre el momento de la llegada. Los peregrinos caminaban días, y la alegría aquí es que sus pies por fin pisan las puertas.",
 fr="Cantique des montées sur le moment de l’arrivée. Les pèlerins marchaient des jours, et la joie ici est que leurs pieds foulent enfin les portes.",
 de="Ein Wallfahrtslied über den Augenblick der Ankunft. Pilger gingen tagelang, und die Freude hier ist, dass ihre Füße endlich in den Toren stehen."),
"psa-125-2": dict(
 es="Cántico de las subidas. La imagen es literal: Jerusalén está en un anillo de colinas, y los peregrinos las veían durante toda la subida.",
 fr="Cantique des montées. L’image est littérale : Jérusalem se tient dans un cercle de collines, et les pèlerins les voyaient tout au long de la montée.",
 de="Ein Wallfahrtslied. Das Bild ist wörtlich: Jerusalem liegt in einem Kranz von Hügeln, und die Pilger sahen sie den ganzen Aufstieg lang."),
"psa-131-2": dict(
 es="El más corto de los salmos de David. La imagen es precisa: un niño destetado ya no exige leche y simplemente se echa junto a su madre.",
 fr="Le plus court des psaumes de David. L’image est précise : un enfant sevré ne réclame plus le lait et se tient simplement contre sa mère.",
 de="Der kürzeste Psalm Davids. Das Bild ist genau: ein entwöhntes Kind verlangt keine Milch mehr und liegt einfach neben seiner Mutter."),
"psa-134-1": dict(
 es="Último cántico de las subidas, dirigido a quienes hacían guardia nocturna en el templo. Los peregrinos que se iban lo cantaban a los que quedaban.",
 fr="Dernier cantique des montées, adressé à ceux qui veillaient la nuit au temple. Les pèlerins qui partaient le chantaient à ceux qui restaient.",
 de="Das letzte Wallfahrtslied, an jene gerichtet, die nachts im Tempel Wache hielten. Die abreisenden Pilger sangen es den Bleibenden zu."),
"psa-137-1": dict(
 es="Escrito en el destierro babilónico. A los cautivos les pidieron cantar una de sus canciones para entretener; el salmo trata de la negativa.",
 fr="Écrit dans l’exil babylonien. On demanda aux captifs de chanter un de leurs chants pour distraire ; le psaume parle du refus.",
 de="Im babylonischen Exil geschrieben. Man forderte die Gefangenen auf, eines ihrer Lieder zur Unterhaltung zu singen; der Psalm handelt von der Weigerung."),
"psa-139-7": dict(
 es="David repasa los lugares donde uno podría esconderse: el cielo, la tumba, el otro lado del mar. La lista se hace como intento, no como consuelo.",
 fr="David passe en revue les lieux où l’on pourrait se cacher : le ciel, la tombe, l’autre bout de la mer. La liste est un essai, non une consolation.",
 de="David geht die Orte durch, an denen man sich verbergen könnte: Himmel, Grab, das andere Ende des Meeres. Die Liste ist ein Versuch, kein Trost."),
"psa-141-3": dict(
 es="Oración vespertina de David. Pide que se ponga guardia a su propia boca, es decir, a lo que él mismo no logra gobernar.",
 fr="Prière du soir de David. Il demande qu’une garde soit mise à sa propre bouche, c’est-à-dire à ce qu’il ne parvient pas à gouverner lui-même.",
 de="Ein Abendgebet Davids. Er bittet, eine Wache vor seinen eigenen Mund zu stellen — vor das, was er selbst nicht beherrscht."),
"psa-142-4": dict(
 es="El encabezado sitúa este salmo cuando David se escondía en una cueva. Escribe que mira a su derecha y no ve a nadie que lo conozca.",
 fr="Le titre situe ce psaume quand David se cachait dans une grotte. Il écrit qu’il regarde à sa droite et ne voit personne qui le connaisse.",
 de="Die Überschrift verortet diesen Psalm in der Zeit, als David sich in einer Höhle verbarg. Er schreibt, er blicke nach rechts und sehe niemanden, der ihn kennt."),
"psa-146-5": dict(
 es="El salmo advierte contra apoyarse en príncipes, porque su aliento se va y sus planes mueren ese mismo día. El consejo es práctico, no poético.",
 fr="Le psaume met en garde contre l’appui sur les princes : leur souffle s’en va et leurs projets meurent le jour même. Le conseil est pratique, non poétique.",
 de="Der Psalm warnt davor, sich auf Fürsten zu stützen: ihr Atem vergeht, und ihre Pläne sterben am selben Tag. Der Rat ist praktisch, nicht poetisch."),
"pro-11-25": dict(
 es="De una colección de dichos breves. La imagen es agrícola: la generosidad se describe como regar, y quien riega también se moja.",
 fr="D’un recueil de courtes sentences. L’image est agricole : la générosité est décrite comme un arrosage où celui qui arrose se mouille aussi.",
 de="Aus einer Sammlung kurzer Sprüche. Das Bild ist bäuerlich: Großzügigkeit wird als Bewässern beschrieben, bei dem der Bewässernde selbst nass wird."),
"pro-12-25": dict(
 es="Observación de que la inquietud pesa físicamente sobre una persona. El remedio que se nombra es sencillo y accesible a cualquiera: una buena palabra.",
 fr="Observation que l’inquiétude pèse physiquement sur une personne. Le remède nommé est simple et à la portée de tous : une bonne parole.",
 de="Eine Beobachtung, dass Sorge einen Menschen körperlich niederdrückt. Das genannte Mittel ist einfach und für jeden verfügbar: ein gutes Wort."),
"pro-15-1": dict(
 es="Dicho de una colección de corte: estas reglas se reunían para quienes tendrían que hablar con reyes y llevar negociaciones.",
 fr="Sentence d’un recueil de cour : de telles règles étaient rassemblées pour ceux qui devraient parler aux rois et mener des négociations.",
 de="Ein Spruch aus einer höfischen Sammlung: solche Regeln wurden für Leute gesammelt, die mit Königen sprechen und verhandeln mussten."),
"pro-24-16": dict(
 es="En el cómputo hebreo, siete no es un número exacto sino «cuantas veces sea». La línea no describe ser impecable, sino poder levantarse.",
 fr="Dans le compte hébreu, sept n’est pas un nombre exact mais « autant de fois qu’il faut ». La ligne ne dit pas être irréprochable, mais pouvoir se relever.",
 de="In hebräischer Zählung ist sieben keine genaue Zahl, sondern „beliebig oft“. Die Zeile beschreibt nicht Fehlerlosigkeit, sondern die Fähigkeit aufzustehen."),
"pro-27-17": dict(
 es="Imagen de fragua: el hierro se afila con hierro, y el proceso es ruidoso y suelta chispas. El dicho no trata del acuerdo, sino del roce.",
 fr="Image de forge : le fer s’aiguise par le fer, et le procédé est bruyant et fait des étincelles. La sentence ne parle pas d’accord, mais de friction.",
 de="Ein Schmiedebild: Eisen wird an Eisen geschärft, und der Vorgang ist laut und schlägt Funken. Der Spruch handelt nicht von Einigkeit, sondern von Reibung."),
"pro-29-25": dict(
 es="El «lazo» aquí es la trampa de un cazador para pájaros. El dicho trata del miedo a las personas, no del miedo al peligro.",
 fr="Le « piège » ici est celui d’un chasseur d’oiseaux. La sentence parle de la peur des gens, non de la peur du danger.",
 de="Die „Schlinge“ ist hier die Vogelfalle eines Jägers. Der Spruch handelt von der Furcht vor Menschen, nicht von der Furcht vor Gefahr."),
"ecc-9-11": dict(
 es="El autor lo enumera: los veloces no siempre ganan la carrera, los sabios no siempre comen. Es una observación que va contra el resto de Proverbios.",
 fr="L’auteur l’énumère : les rapides ne gagnent pas toujours la course, les sages ne mangent pas toujours. C’est une observation qui contredit les Proverbes.",
 de="Der Verfasser zählt es auf: die Schnellen gewinnen nicht immer den Lauf, die Weisen haben nicht immer Brot. Eine Beobachtung gegen den Rest der Sprüche."),
"ecc-12-13": dict(
 es="Líneas finales de un libro que ha llamado vapor a todo. La conclusión es breve y deliberadamente modesta, tras doce capítulos de probar opciones.",
 fr="Lignes finales d’un livre qui a tout appelé vapeur. La conclusion est brève et volontairement modeste, après douze chapitres d’essais.",
 de="Die Schlusszeilen eines Buches, das alles Windhauch genannt hat. Der Schluss ist kurz und bewusst bescheiden, nach zwölf Kapiteln des Ausprobierens."),
"sng-8-6": dict(
 es="De un libro que nunca menciona a Dios y consiste enteramente en dos amantes que hablan. Un sello sobre el corazón es imagen de propiedad, no de adorno.",
 fr="D’un livre qui ne mentionne jamais Dieu et n’est fait que de deux amants qui parlent. Un sceau sur le cœur est une image de propriété, non d’ornement.",
 de="Aus einem Buch, das Gott nie erwähnt und ganz aus dem Gespräch zweier Liebender besteht. Ein Siegel auf dem Herzen bedeutet Besitz, nicht Schmuck."),
"isa-1-18": dict(
 es="Dicho al abrirse el libro, justo tras la acusación de ofrecer sacrificios mientras se aplasta a los pobres. El tinte carmesí de entonces no se iba.",
 fr="Dit à l’ouverture du livre, juste après l’accusation d’offrir des sacrifices tout en écrasant les pauvres. La teinture cramoisie d’alors ne partait pas.",
 de="Gesagt am Anfang des Buches, direkt nach dem Vorwurf, Opfer zu bringen und dabei die Armen zu zermalmen. Der Purpurfarbstoff jener Zeit ging nicht heraus."),

# ── партия 3 ──────────────────────────────────────────────────────────────
"isa-9-2": dict(
 es="Dicho de los distritos del norte que Asiria devastó primero. El Evangelio de Mateo aplicará después esta línea al inicio del ministerio en Galilea.",
 fr="Dit des districts du nord qu’Assur dévasta les premiers. L’Évangile de Matthieu appliquera plus tard cette ligne au début du ministère en Galilée.",
 de="Gesagt über die Nordbezirke, die Assyrien zuerst verwüstete. Das Matthäusevangelium bezieht diese Zeile später auf den Beginn des Wirkens in Galiläa."),
"isa-35-3": dict(
 es="Dirigido no a los fuertes, sino a quienes deben sostener a otros: fortalece manos ajenas, habla al corazón ajeno. La tarea se entrega a personas.",
 fr="Adressé non aux forts, mais à ceux qui doivent en soutenir d’autres : fortifiez des mains étrangères, parlez à un cœur étranger. La tâche est confiée à des gens.",
 de="Nicht an die Starken gerichtet, sondern an die, die andere stützen sollen: stärkt fremde Hände, redet fremden Herzen zu. Die Aufgabe wird Menschen übergeben."),
"isa-40-11": dict(
 es="Viene justo después de líneas sobre el poder que sostiene aguas y montes. La escala cambia de golpe: el mismo lleva corderos en el pliegue del manto.",
 fr="Cela vient juste après des lignes sur la puissance qui tient les eaux et les montagnes. L’échelle change d’un coup : le même porte des agneaux contre lui.",
 de="Es folgt direkt auf Zeilen über die Macht, die Wasser und Berge hält. Der Maßstab kippt abrupt: derselbe trägt Lämmer in seinem Gewandbausch."),
"isa-42-3": dict(
 es="Una caña quebrada y una mecha humeante son cosas que normalmente se tiran. La línea describe cómo las tratará el siervo del Señor.",
 fr="Un roseau brisé et une mèche fumante sont des choses qu’on jette d’ordinaire. La ligne décrit comment le serviteur du Seigneur les traitera.",
 de="Ein geknicktes Rohr und ein glimmender Docht sind Dinge, die man sonst wegwirft. Die Zeile beschreibt, wie der Knecht des Herrn mit ihnen umgeht."),
"isa-46-4": dict(
 es="Dicho por contraste con los ídolos babilonios, llevados a hombros en las fiestas. Aquí se invierte: no se lleva al dios, sino a la persona, hasta las canas.",
 fr="Dit par contraste avec les idoles babyloniennes, portées sur les épaules aux fêtes. Ici c’est l’inverse : on ne porte pas le dieu mais l’homme, jusqu’aux cheveux blancs.",
 de="Gesagt im Gegensatz zu babylonischen Götzen, die man an Festen auf Schultern trug. Hier ist es umgekehrt: nicht der Gott wird getragen, sondern der Mensch, bis ins Greisenalter."),
"isa-49-15": dict(
 es="Respuesta a un pueblo que decía haber sido olvidado. El profeta toma la comparación más imposible que hay y dice que ni siquiera esa alcanza.",
 fr="Réponse à un peuple qui se disait oublié. Le prophète prend la comparaison la plus impossible qui soit et dit que même elle ne suffit pas.",
 de="Die Antwort an ein Volk, das sich vergessen glaubte. Der Prophet nimmt den unmöglichsten Vergleich, den es gibt, und sagt, selbst der reiche nicht aus."),
"isa-50-4": dict(
 es="De un canto del siervo. Saber sostener al cansado se describe como algo que se enseña mañana tras mañana, más como un oficio que como un don.",
 fr="D’un chant du serviteur. Savoir soutenir celui qui est las est décrit comme un enseignement reçu matin après matin, plus un métier qu’un don.",
 de="Aus einem Knechtslied. Zu wissen, wie man Müde stützt, wird als etwas beschrieben, das Morgen für Morgen gelehrt wird — eher Handwerk als Gabe."),
"isa-54-10": dict(
 es="Dicho a un pueblo tras la catástrofe, en un capítulo que llama a Jerusalén esposa abandonada. Los montes se toman como imagen de lo más estable que se conoce.",
 fr="Dit à un peuple après la catastrophe, dans un chapitre qui appelle Jérusalem épouse délaissée. Les montagnes servent d’image de ce qu’on connaît de plus stable.",
 de="Gesagt zu einem Volk nach der Katastrophe, in einem Kapitel, das Jerusalem eine verlassene Frau nennt. Berge stehen für das Beständigste, was ein Mensch kennt."),
"isa-58-11": dict(
 es="La promesa es condicional: antes va la exigencia de dar de comer al hambriento y acoger al sin techo. El huerto regado premia eso, no el ayuno.",
 fr="La promesse est conditionnelle : avant elle vient l’exigence de nourrir l’affamé et d’abriter le sans-logis. Le jardin arrosé récompense cela, non le jeûne.",
 de="Die Zusage ist bedingt: davor steht die Forderung, Hungrige zu speisen und Obdachlose aufzunehmen. Der bewässerte Garten belohnt das, nicht das Fasten."),
"jer-1-5": dict(
 es="Jeremías responde que es demasiado joven y no sabe hablar. La tarea a la que se le llama durará cuarenta años y no le traerá ningún éxito.",
 fr="Jérémie répond qu’il est trop jeune et ne sait pas parler. La tâche à laquelle il est appelé durera quarante ans et ne lui apportera aucun succès.",
 de="Jeremia antwortet, er sei zu jung und könne nicht reden. Die Aufgabe, zu der er gerufen wird, dauert vierzig Jahre und bringt ihm keinen Erfolg."),
"jer-6-16": dict(
 es="Dicho en una encrucijada: el profeta aconseja detenerse y preguntar por los senderos antiguos. El texto dice que el pueblo respondió que no andaría por ellos.",
 fr="Dit à un carrefour : le prophète conseille de s’arrêter et de s’enquérir des sentiers anciens. Le texte dit que le peuple répondit qu’il n’y marcherait pas.",
 de="Gesagt an einer Wegkreuzung: der Prophet rät, stehenzubleiben und nach den alten Pfaden zu fragen. Der Text sagt, das Volk antwortete, es werde sie nicht gehen."),
"jer-32-17": dict(
 es="Jeremías ora bajo custodia en una ciudad sitiada, tras haber comprado un campo que los babilonios están a punto de ocupar.",
 fr="Jérémie prie sous garde dans une ville assiégée, après avoir acheté un champ que les Babyloniens sont sur le point d’occuper.",
 de="Jeremia betet unter Bewachung in einer belagerten Stadt, nachdem er gerade einen Acker gekauft hat, den die Babylonier gleich besetzen werden."),
"jer-33-3": dict(
 es="Dicho a un profeta encerrado en el patio de la guardia, sin poder salir. La promesa se refiere a cosas que aún no conoce.",
 fr="Dit à un prophète enfermé dans la cour de la garde, sans pouvoir sortir. La promesse concerne des choses qu’il ignore encore.",
 de="Gesagt zu einem Propheten, der im Wachhof eingeschlossen ist und nicht hinauskann. Die Zusage betrifft Dinge, die er noch nicht kennt."),
"lam-3-26": dict(
 es="Del lamento por Jerusalén destruida. La palabra traducida «bueno» está junto a «en silencio»: el consejo es esperar sin palabras.",
 fr="Du chant de deuil sur Jérusalem détruite. Le mot rendu par « bon » côtoie « en silence » : le conseil porte sur une attente sans paroles.",
 de="Aus der Klage über das zerstörte Jerusalem. Das mit „gut“ übersetzte Wort steht neben „stille“ — der Rat gilt einem Warten ohne Worte."),
"ezk-34-16": dict(
 es="Dicho en un capítulo donde los pastores son los gobernantes que se apacentaban a sí mismos en vez del rebaño. La promesa viene a sustituirlos.",
 fr="Dit dans un chapitre où les bergers sont les dirigeants qui se nourrissaient eux-mêmes au lieu du troupeau. La promesse vient les remplacer.",
 de="Gesagt in einem Kapitel, in dem die Hirten die Herrscher sind, die sich selbst weideten statt die Herde. Die Zusage tritt an ihre Stelle."),
"ezk-37-3": dict(
 es="La pregunta se hace en medio de un valle lleno de huesos secos. Ezequiel no responde «sí» sino «tú lo sabes», y es la única respuesta honesta posible.",
 fr="La question est posée au milieu d’une vallée pleine d’ossements desséchés. Ézéchiel ne répond pas « oui » mais « tu le sais » : la seule réponse honnête possible.",
 de="Die Frage wird mitten in einem Tal voller dürrer Gebeine gestellt. Ezechiel antwortet nicht „ja“, sondern „du weißt es“ — die einzige ehrliche Antwort."),
"dan-6-10": dict(
 es="El decreto ya está firmado y la oración prohibida bajo pena de muerte durante treinta días. Daniel abre sus ventanas y ora como siempre, tres veces al día.",
 fr="Le décret est déjà signé et la prière interdite sous peine de mort pendant trente jours. Daniel ouvre ses fenêtres et prie comme d’habitude, trois fois par jour.",
 de="Der Erlass ist bereits unterzeichnet, Beten dreißig Tage lang bei Todesstrafe verboten. Daniel öffnet seine Fenster und betet wie immer, dreimal am Tag."),
"jol-2-13": dict(
 es="Rasgarse la ropa era el signo aceptado de duelo, visible para todos. El profeta propone en su lugar algo que nadie verá.",
 fr="Déchirer ses vêtements était le signe reconnu du deuil, visible de tous. Le prophète propose à la place quelque chose que personne ne verra.",
 de="Das Zerreißen der Kleider war das anerkannte Zeichen der Trauer, für alle sichtbar. Der Prophet schlägt stattdessen etwas vor, das niemand sieht."),
"amo-5-24": dict(
 es="Dicho a gente cuyo culto estaba en perfecto orden. El profeta dice que no soporta escuchar sus cantos, y exige otra cosa en su lugar.",
 fr="Dit à des gens dont le culte était en parfait ordre. Le prophète dit qu’il ne supporte pas d’écouter leurs chants, et exige autre chose à la place.",
 de="Gesagt zu Leuten, deren Gottesdienst tadellos geordnet war. Der Prophet sagt, er ertrage ihre Lieder nicht, und fordert stattdessen etwas anderes."),
"jon-2-2": dict(
 es="Jonás ora desde dentro del pez, adonde fue a parar huyendo de un encargo. Él mismo había pedido a los marineros que lo echaran al mar.",
 fr="Jonas prie depuis l’intérieur du poisson, où il a échoué en fuyant une mission. C’est lui-même qui avait demandé aux marins de le jeter à la mer.",
 de="Jona betet aus dem Bauch des Fisches, wohin er auf der Flucht vor einem Auftrag geriet. Er selbst hatte die Seeleute gebeten, ihn ins Meer zu werfen."),
"mic-7-8": dict(
 es="Dicho en un capítulo donde el profeta se queja de que no queda gente honrada y ni de los de casa puede uno fiarse. La línea sobre caer viene tras eso.",
 fr="Dit dans un chapitre où le prophète se plaint qu’il ne reste plus d’honnêtes gens et qu’on ne peut se fier même aux siens. La ligne sur la chute suit.",
 de="Gesagt in einem Kapitel, in dem der Prophet klagt, es gebe keine redlichen Menschen mehr und nicht einmal den Hausgenossen sei zu trauen."),
"nam-1-7": dict(
 es="El libro trata entero de la caída de Nínive, capital de un imperio que había asolado medio mundo conocido. La línea sobre el refugio está dentro de esa profecía.",
 fr="Le livre porte entièrement sur la chute de Ninive, capitale d’un empire qui avait ravagé la moitié du monde connu. La ligne sur le refuge est dans cette prophétie.",
 de="Das Buch handelt ganz vom Fall Ninives, der Hauptstadt eines Reiches, das die halbe bekannte Welt verwüstet hatte. Die Zeile über die Zuflucht steht darin."),
"hab-2-3": dict(
 es="Respuesta a un profeta que se puso en su puesto y exigió una explicación. Se le dice que escriba la visión con letras grandes, para leerla al pasar corriendo.",
 fr="Réponse à un prophète qui a pris son poste et exigé une explication. On lui dit d’écrire la vision assez grand pour être lue en courant.",
 de="Die Antwort an einen Propheten, der sich auf seinen Posten stellte und eine Erklärung verlangte. Er soll die Schau so groß schreiben, dass man sie im Laufen liest."),
"zec-4-6": dict(
 es="Dicho a un hombre que debe terminar un templo con un puñado de desterrados que volvieron. El profeta pregunta luego quién desprecia el día de los comienzos pequeños.",
 fr="Dit à un homme qui doit achever un temple avec une poignée d’exilés revenus. Le prophète demande ensuite qui méprise le jour des petits commencements.",
 de="Gesagt zu einem Mann, der einen Tempel mit einer Handvoll Heimgekehrter fertigstellen soll. Der Prophet fragt danach, wer den Tag der kleinen Anfänge verachtet."),
"mal-3-10": dict(
 es="El único lugar donde se invita a una prueba: el profeta dice «ponedme a prueba». Dicho a gente que traía animales enfermos como ofrenda.",
 fr="Le seul endroit où une épreuve est proposée : le prophète dit « mettez-moi à l’épreuve ». Dit à des gens qui apportaient des bêtes malades en offrande.",
 de="Die einzige Stelle, an der eine Probe eingeladen wird: der Prophet sagt „stellt mich auf die Probe“. Gesagt zu Leuten, die kranke Tiere als Opfer brachten."),
"mat-4-4": dict(
 es="Respuesta a la primera tentación, tras cuarenta días sin comer. Jesús cita el Deuteronomio: palabras dichas a un pueblo también en un desierto, también con hambre.",
 fr="Réponse à la première tentation, après quarante jours sans manger. Jésus cite le Deutéronome : des mots dits à un peuple aussi au désert, aussi affamé.",
 de="Die Antwort auf die erste Versuchung, nach vierzig Tagen ohne Essen. Jesus zitiert das Deuteronomium — Worte an ein Volk, ebenfalls in der Wüste, ebenfalls hungrig."),
"mat-6-21": dict(
 es="Del Sermón del Monte. El orden es el inverso del esperado: el tesoro se nombra como causa y el corazón como efecto, no al revés.",
 fr="Du Sermon sur la montagne. L’ordre est l’inverse de celui qu’on attend : le trésor est nommé comme cause et le cœur comme effet, non l’inverse.",
 de="Aus der Bergpredigt. Die Reihenfolge ist umgekehrt als erwartet: der Schatz wird als Ursache genannt und das Herz als Folge, nicht andersherum."),
"mat-6-33": dict(
 es="Está en medio de una charla sobre comida y ropa, dirigida a gente que tenía un solo manto. No trata de ambición, sino de subsistencia.",
 fr="Cela se tient au milieu d’un propos sur la nourriture et le vêtement, adressé à des gens qui n’avaient qu’un manteau. Il ne s’agit pas d’ambition mais de survie.",
 de="Es steht mitten in einer Rede über Essen und Kleidung, gerichtet an Menschen mit einem einzigen Mantel. Es geht nicht um Ehrgeiz, sondern ums Auskommen."),
"mat-9-36": dict(
 es="Dicho de la multitud que Jesús vio al recorrer las aldeas. El verbo griego significa aquí un apretón físico por dentro, no compasión en general.",
 fr="Dit de la foule que Jésus vit en parcourant les bourgs. Le verbe grec désigne ici une crispation physique intérieure, non une compassion générale.",
 de="Gesagt über die Menge, die Jesus beim Durchziehen der Orte sah. Das griechische Verb meint ein körperliches Zusammenziehen im Innern, nicht allgemeines Mitgefühl."),
"mat-14-27": dict(
 es="Noche, mitad del lago, la barca golpeada por las olas durante horas. Los discípulos gritan de miedo, tomando por un fantasma la figura que se acerca.",
 fr="La nuit, au milieu du lac, la barque battue par les vagues depuis des heures. Les disciples crient de peur, prenant pour un fantôme la figure qui approche.",
 de="Nacht, Mitte des Sees, das Boot seit Stunden von Wellen geschlagen. Die Jünger schreien vor Furcht und halten die herankommende Gestalt für ein Gespenst."),
"mat-16-24": dict(
 es="Dicho después de que Pedro intentara disuadirlo de morir. Los oyentes veían cruces junto a los caminos y entendían la imagen al pie de la letra.",
 fr="Dit après que Pierre eut tenté de l’en dissuader. Les auditeurs voyaient des croix le long des routes et comprenaient l’image au sens propre.",
 de="Gesagt, nachdem Petrus ihn vom Sterben abbringen wollte. Die Zuhörer sahen Kreuze an den Straßen und verstanden das Bild wörtlich."),
"mat-25-40": dict(
 es="De una escena de juicio donde ambos bandos se sorprenden por igual. Ninguno de los dos sabía a quién había estado ayudando, o dejando de ayudar.",
 fr="D’une scène de jugement où les deux camps sont également surpris. Ni l’un ni l’autre ne savait qui il avait en fait aidé, ou omis d’aider.",
 de="Aus einer Gerichtsszene, in der beide Seiten gleichermaßen überrascht sind. Keine wusste, wem sie tatsächlich geholfen oder nicht geholfen hatte."),
"mat-26-39": dict(
 es="Dicho de noche en un huerto, con el rostro en tierra, horas antes del arresto. Justo antes dice a los discípulos que su alma está triste hasta la muerte.",
 fr="Dit la nuit dans un jardin, face contre terre, quelques heures avant l’arrestation. Juste avant, il dit aux disciples que son âme est triste jusqu’à la mort.",
 de="Nachts in einem Garten gesagt, das Gesicht am Boden, Stunden vor der Verhaftung. Kurz zuvor sagt er den Jüngern, seine Seele sei betrübt bis zum Tod."),
"mrk-1-35": dict(
 es="El día anterior había sido largo de curaciones, con el pueblo entero a la puerta hasta la noche. Se levanta antes del alba y sale solo; lo van a buscar.",
 fr="La veille avait été une longue journée de guérisons, toute la ville à la porte jusqu’à la nuit. Il se lève avant l’aube et part seul ; on part le chercher.",
 de="Der Vortag war ein langer Tag voller Heilungen, die ganze Stadt bis in die Nacht vor der Tür. Er steht vor Tagesanbruch auf und geht allein fort."),
"mrk-4-39": dict(
 es="Tormenta en el lago, la barca anegándose, y él duerme en la popa. Los discípulos lo despiertan preguntándole si no le importa que perezcan.",
 fr="Tempête sur le lac, la barque qui se remplit, et lui dort à la poupe. Les disciples le réveillent en demandant s’il se moque qu’ils périssent.",
 de="Sturm auf dem See, das Boot läuft voll, und er schläft im Heck. Die Jünger wecken ihn mit der Frage, ob es ihn nicht kümmere, dass sie umkommen."),
"mrk-5-34": dict(
 es="Dicho a una mujer que sangraba desde hacía doce años. Por la ley era impura y no tenía derecho a tocar a nadie, por eso se acercó por detrás.",
 fr="Dit à une femme qui saignait depuis douze ans. Selon la loi elle était impure et n’avait pas le droit de toucher quiconque : d’où son approche par-derrière.",
 de="Gesagt zu einer Frau, die zwölf Jahre lang blutete. Nach dem Gesetz war sie unrein und durfte niemanden berühren — darum kam sie von hinten."),
"mrk-6-31": dict(
 es="Dicho a discípulos que vuelven de su primer viaje solos. La razón se da allí mismo: iba y venía tanta gente que no tenían tiempo ni de comer.",
 fr="Dit à des disciples revenant de leur première tournée seuls. La raison est donnée sur place : tant de gens allaient et venaient qu’ils n’avaient pas le temps de manger.",
 de="Gesagt zu Jüngern, die von ihrer ersten Reise allein zurückkommen. Der Grund steht gleich dabei: so viele kamen und gingen, dass sie nicht zum Essen kamen."),
"mrk-12-41": dict(
 es="Jesús se sienta frente al arca de las ofrendas y mira a la gente echar dinero. No mide lo que se da, sino cuánto le quedó a quien lo dio.",
 fr="Jésus s’assoit face au tronc et regarde les gens y mettre de l’argent. Il ne mesure pas ce qui est donné, mais ce qui reste à celui qui donne.",
 de="Jesus setzt sich dem Opferkasten gegenüber und sieht zu, wie Leute Geld einwerfen. Er misst nicht die Gabe, sondern was dem Geber danach bleibt."),
"luk-2-10": dict(
 es="Dicho a pastores en un campo de noche: hombres cuyo trabajo los volvía ritualmente impuros y a quienes no se invitaba a ninguna parte.",
 fr="Dit à des bergers dans un champ, la nuit : des hommes que leur travail rendait rituellement impurs et qu’on n’invitait nulle part.",
 de="Gesagt zu Hirten nachts auf dem Feld — Männern, die ihre Arbeit kultisch unrein machte und die nirgendwohin eingeladen wurden."),
"luk-5-16": dict(
 es="Cuanta más gente se reunía, más a menudo se retiraba. Lucas lo anota no como excepción, sino como costumbre permanente.",
 fr="Plus les gens s’assemblaient, plus souvent il se retirait. Luc le note non comme une exception mais comme une habitude constante.",
 de="Je mehr Menschen zusammenkamen, desto häufiger zog er sich zurück. Lukas notiert das nicht als Ausnahme, sondern als ständige Gewohnheit."),
"luk-7-13": dict(
 es="Dicho a una viuda que entierra a su hijo único. Se quedaba sin un solo hombre en la casa, lo que en aquel tiempo significaba la miseria.",
 fr="Dit à une veuve qui enterre son fils unique. Elle restait sans aucun homme dans la maison, ce qui à l’époque signifiait la misère.",
 de="Gesagt zu einer Witwe, die ihren einzigen Sohn begräbt. Sie blieb ohne einen einzigen Mann im Haus zurück, was damals Mittellosigkeit bedeutete."),
"luk-12-15": dict(
 es="Respuesta a un hombre que le pidió resolver un pleito de herencia con su hermano. Jesús se niega a ser juez y habla de algo completamente distinto.",
 fr="Réponse à un homme qui lui demandait de trancher un litige d’héritage avec son frère. Jésus refuse d’être juge et parle de tout autre chose.",
 de="Die Antwort an einen Mann, der ihn um die Schlichtung eines Erbstreits mit dem Bruder bat. Jesus lehnt das Richteramt ab und spricht von etwas ganz anderem."),
"luk-12-32": dict(
 es="La expresión «pequeño rebaño» habla de tamaño: los oyentes eran pocos y lo sabían. Dicho justo después de la charla sobre comida y ropa.",
 fr="L’expression « petit troupeau » parle de taille : les auditeurs étaient peu nombreux et le savaient. Dit juste après le propos sur la nourriture et le vêtement.",
 de="Der Ausdruck „kleine Herde“ meint die Größe: die Zuhörer waren wenige und wussten es. Gesagt direkt nach der Rede über Essen und Kleidung."),
"luk-17-5": dict(
 es="Los apóstoles piden más fe justo después de que se les diga que perdonen siete veces al día. La respuesta sobre el grano de mostaza habla de tamaño, no de cantidad.",
 fr="Les apôtres demandent plus de foi juste après qu’on leur a dit de pardonner sept fois par jour. La réponse sur le grain de moutarde parle de taille, non de quantité.",
 de="Die Apostel bitten um mehr Glauben, direkt nachdem sie siebenmal täglich vergeben sollen. Die Antwort vom Senfkorn spricht von Größe, nicht von Menge."),
"luk-18-1": dict(
 es="Introducción a una parábola sobre una viuda que siguió acudiendo a un juez corrupto hasta que cedió. Lucas dice sin rodeos para qué sirve la parábola.",
 fr="Introduction à une parabole sur une veuve qui revint sans cesse chez un juge corrompu jusqu’à ce qu’il cède. Luc dit franchement à quoi sert la parabole.",
 de="Die Einleitung zu einem Gleichnis über eine Witwe, die so lange zu einem korrupten Richter ging, bis er nachgab. Lukas sagt geradeheraus, wozu es dient."),
"luk-19-10": dict(
 es="Dicho en casa de Zaqueo, un recaudador a quien toda la ciudad tenía por traidor. La multitud murmuraba fuera porque había entrado en casa de semejante hombre.",
 fr="Dit chez Zachée, un collecteur d’impôts que toute la ville tenait pour un traître. La foule murmurait dehors qu’il était entré chez un tel homme.",
 de="Gesagt im Haus des Zachäus, eines Zöllners, den die ganze Stadt für einen Verräter hielt. Draußen murrte die Menge, dass er bei so einem einkehrte."),
"luk-24-32": dict(
 es="Dos discípulos salían de Jerusalén comentando la ejecución y no reconocieron a su acompañante. Se dieron cuenta de quién era solo después de que desapareciera.",
 fr="Deux disciples sortaient de Jérusalem en parlant de l’exécution et ne reconnurent pas leur compagnon. Ils comprirent qui il était seulement après sa disparition.",
 de="Zwei Jünger gingen aus Jerusalem hinaus und sprachen über die Hinrichtung, ohne ihren Begleiter zu erkennen. Erst als er verschwand, begriffen sie, wer er war."),
"jhn-4-14": dict(
 es="Dicho junto a un pozo al mediodía a una samaritana que iba por agua a la hora más calurosa para no encontrarse con las otras mujeres del pueblo.",
 fr="Dit près d’un puits à midi à une Samaritaine venue puiser à l’heure la plus chaude pour éviter les autres femmes du village.",
 de="Gesagt an einem Brunnen zur Mittagszeit zu einer Samariterin, die zur heißesten Stunde Wasser holte, um den anderen Frauen des Dorfes auszuweichen."),
"jhn-6-35": dict(
 es="Dicho al día siguiente de dar de comer a cinco mil. La multitud volvió, y él dice sin rodeos que no buscan una señal, sino comida.",
 fr="Dit le lendemain du repas des cinq mille. La foule est revenue, et il dit franchement qu’elle ne cherche pas un signe mais de la nourriture.",
 de="Gesagt am Tag nach der Speisung der Fünftausend. Die Menge kam zurück, und er sagt offen, sie suche kein Zeichen, sondern Essen."),
"jhn-9-25": dict(
 es="Dicho por un hombre ciego de nacimiento, en un interrogatorio montado para arrancarle una respuesta concreta. Se niega a discutir teología y se atiene a lo que sabe.",
 fr="Dit par un homme aveugle de naissance, lors d’un interrogatoire monté pour lui arracher une réponse précise. Il refuse de discuter théologie et s’en tient à ce qu’il sait.",
 de="Gesagt von einem Blindgeborenen, in einem Verhör, das eine bestimmte Antwort erzwingen sollte. Er weigert sich, über Theologie zu streiten, und bleibt beim Gewussten."),
"jhn-12-24": dict(
 es="Dicho días antes de la ejecución, cuando unos griegos pidieron verlo. Su respuesta no trata del encuentro, sino de lo que debe ocurrirle a él.",
 fr="Dit quelques jours avant l’exécution, quand des Grecs demandèrent à le voir. Sa réponse ne porte pas sur la rencontre mais sur ce qui doit lui arriver.",
 de="Gesagt Tage vor der Hinrichtung, als einige Griechen ihn sehen wollten. Seine Antwort handelt nicht von der Begegnung, sondern davon, was ihm geschehen muss."),
"jhn-14-1": dict(
 es="Primera línea del discurso de despedida, dicha inmediatamente después de advertir a Pedro sobre la negación. Los discípulos en ese momento están conmocionados.",
 fr="Première ligne du discours d’adieu, dite juste après avoir averti Pierre du reniement. Les disciples à cet instant sont ébranlés.",
 de="Die erste Zeile der Abschiedsrede, gesagt unmittelbar nachdem er Petrus die Verleugnung ankündigte. Die Jünger sind in diesem Augenblick erschüttert."),
"jhn-15-5": dict(
 es="Dicho camino del huerto, quizá pasando junto a viñas fuera de la ciudad. La imagen era literal: un sarmiento cortado de la vid no dura ni un día.",
 fr="Dit en chemin vers le jardin, peut-être le long des vignes hors de la ville. L’image était littérale : un sarment coupé du cep ne tient pas un jour.",
 de="Gesagt auf dem Weg zum Garten, vielleicht an Weinbergen vor der Stadt vorbei. Das Bild war wörtlich: eine Rebe ohne Weinstock hält keinen Tag."),
"jhn-16-22": dict(
 es="Jesús compara lo que viene con un parto: el dolor no se anula ni se acorta, pero deja de ser lo principal una vez pasado.",
 fr="Jésus compare ce qui vient à un accouchement : la douleur n’est ni annulée ni abrégée, mais cesse d’être l’essentiel une fois passée.",
 de="Jesus vergleicht das Kommende mit einer Geburt: der Schmerz wird weder aufgehoben noch verkürzt, hört aber danach auf, die Hauptsache zu sein."),
"jhn-21-17": dict(
 es="Pedro lo negó tres veces junto a un fuego en un patio, y ahora se le pregunta tres veces junto a otro fuego, en la orilla. La cuenta coincide con las negaciones.",
 fr="Pierre l’a renié trois fois près d’un feu dans une cour, et on l’interroge trois fois près d’un autre feu, sur le rivage. Le compte égale celui des reniements.",
 de="Petrus verleugnete ihn dreimal an einem Feuer im Hof, und nun wird er dreimal an einem anderen Feuer am Ufer gefragt. Die Zahl entspricht den Verleugnungen."),
"act-4-13": dict(
 es="Así describe a Pedro y Juan el consejo dirigente, un órgano culto que juzgaba su caso. La palabra no significa tontos, sino sin estudios.",
 fr="C’est ainsi que le conseil dirigeant, instance instruite qui jugeait leur cas, décrit Pierre et Jean. Le mot ne signifie pas sots, mais sans instruction.",
 de="So beschreibt der herrschende Rat, ein gebildetes Gremium, das ihren Fall verhandelte, Petrus und Johannes. Das Wort heißt nicht dumm, sondern ungelehrt."),
"act-16-25": dict(
 es="A Pablo y Silas los habían azotado con varas y encerrado en la prisión interior con los pies en el cepo. Es medianoche, y los demás presos escuchan.",
 fr="Paul et Silas avaient été battus de verges et enfermés dans la prison intérieure, les pieds aux ceps. Il est minuit, et les autres prisonniers écoutent.",
 de="Paulus und Silas waren mit Ruten geschlagen und im inneren Kerker mit Füßen im Block eingeschlossen worden. Es ist Mitternacht, und die anderen Gefangenen hören zu."),
"act-17-28": dict(
 es="Pablo habla en Atenas ante filósofos y cita no la Escritura sino a un poeta griego, porque aquellos oyentes nunca habían leído las Escrituras.",
 fr="Paul parle à Athènes devant des philosophes et cite non l’Écriture mais un poète grec, car ces auditeurs n’avaient jamais lu les Écritures.",
 de="Paulus spricht in Athen vor Philosophen und zitiert nicht die Schrift, sondern einen griechischen Dichter, weil diese Zuhörer die Schriften nie gelesen hatten."),
"rom-3-23": dict(
 es="Conclusión de un largo razonamiento en que Pablo mostró que gentiles y judíos están en la misma situación. El «todos» de aquí es el resultado de una demostración.",
 fr="Conclusion d’un long raisonnement où Paul a montré que païens et Juifs sont dans la même situation. Le « tous » est ici le résultat d’une démonstration.",
 de="Der Schluss einer langen Beweisführung, in der Paulus zeigte, dass Heiden und Juden gleich dastehen. Das „alle“ ist hier das Ergebnis eines Beweises."),
"rom-8-1": dict(
 es="Viene justo después de un capítulo donde Pablo describe que hace lo que no quiere y se llama a sí mismo miserable. Esta es la respuesta a ese grito.",
 fr="Cela vient juste après un chapitre où Paul décrit qu’il fait ce qu’il ne veut pas et se dit misérable. Voici la réponse à ce cri.",
 de="Es folgt direkt auf ein Kapitel, in dem Paulus beschreibt, dass er tut, was er nicht will, und sich elend nennt. Das ist die Antwort auf diesen Schrei."),
"rom-8-26": dict(
 es="Dicho sobre la situación en que una persona no sabe qué pedir. Pablo no aconseja encontrar las palabras; dice que puede que no haya palabra alguna.",
 fr="Dit à propos de la situation où l’on ne sait pas quoi demander. Paul ne conseille pas de trouver les mots ; il dit qu’il peut n’y avoir aucun mot.",
 de="Gesagt über die Lage, in der ein Mensch nicht weiß, worum er bitten soll. Paulus rät nicht, Worte zu finden; er sagt, es gebe vielleicht keine."),
"rom-8-38": dict(
 es="Final de un capítulo que empezó con la ausencia de condena. Pablo enumera todo lo que se le ocurre, incluidos la muerte y el futuro, y cierra la lista.",
 fr="Fin d’un chapitre qui commençait par l’absence de condamnation. Paul énumère tout ce qui lui vient, y compris la mort et l’avenir, et clôt la liste.",
 de="Das Ende eines Kapitels, das mit der ausbleibenden Verurteilung begann. Paulus zählt alles auf, was ihm einfällt, samt Tod und Zukunft, und schließt die Liste."),
"rom-12-15": dict(
 es="De una lista de instrucciones breves. El orden importa: alegrarse con los que se alegran va primero, y suele costar más que llorar con los que lloran.",
 fr="D’une liste d’instructions brèves. L’ordre compte : se réjouir avec ceux qui se réjouissent vient d’abord, et c’est souvent plus dur que pleurer avec ceux qui pleurent.",
 de="Aus einer Liste kurzer Anweisungen. Die Reihenfolge zählt: sich mit Fröhlichen freuen steht zuerst, und das fällt meist schwerer als das Weinen mit Weinenden."),
"rom-12-21": dict(
 es="Conclusión de una sección sobre cómo tratar a los enemigos. Justo antes Pablo cita los Proverbios y habla de comida y bebida para el adversario.",
 fr="Conclusion d’une section sur la manière de traiter les ennemis. Juste avant, Paul cite les Proverbes et parle de nourriture et de boisson pour l’adversaire.",
 de="Der Schluss eines Abschnitts darüber, wie man mit Feinden umgeht. Kurz davor zitiert Paulus die Sprüche und spricht von Speise und Trank für den Gegner."),
"1co-1-27": dict(
 es="Pablo recuerda a los corintios su propia composición: no muchos sabios, no muchos de buena cuna. Lo dice a una comunidad orgullosa de su espiritualidad.",
 fr="Paul rappelle aux Corinthiens leur propre composition : pas beaucoup de sages, pas beaucoup de bien nés. Il le dit à une communauté fière de sa spiritualité.",
 de="Paulus erinnert die Korinther an ihre eigene Zusammensetzung: nicht viele Weise, nicht viele Vornehme. Er sagt es einer Gemeinde, die auf ihre Geistlichkeit stolz war."),
"1co-15-58": dict(
 es="Última línea del capítulo sobre la resurrección, el razonamiento más largo de Pablo de que la muerte no es definitiva. La conclusión resulta ser sobre el trabajo.",
 fr="Dernière ligne du chapitre sur la résurrection, le plus long raisonnement de Paul contre le caractère définitif de la mort. La conclusion porte sur le travail.",
 de="Die letzte Zeile des Auferstehungskapitels, der längsten Beweisführung des Paulus, dass der Tod nicht endgültig ist. Der Schluss handelt dann von Arbeit."),
"2co-9-7": dict(
 es="De una carta sobre una colecta para los hambrientos de Jerusalén. Pablo pasó años reuniéndola y subraya que la obligación lo estropea todo.",
 fr="D’une lettre sur une collecte pour les affamés de Jérusalem. Paul a passé des années à la rassembler et souligne que la contrainte gâche tout.",
 de="Aus einem Brief über eine Sammlung für die Hungernden in Jerusalem. Paulus sammelte sie jahrelang und betont, dass Zwang die ganze Sache verdirbt."),
"2co-12-10": dict(
 es="Conclusión de su relato sobre una debilidad que no le fue quitada. Pablo enumera insultos y persecuciones como cosas en las que se complace estar.",
 fr="Conclusion de son récit sur une faiblesse qui ne lui fut pas ôtée. Paul énumère outrages et persécutions comme des choses où il se plaît à être.",
 de="Der Schluss seines Berichts über eine Schwäche, die ihm nicht genommen wurde. Paulus zählt Beschimpfungen und Verfolgungen als Zustände auf, in denen er gern ist."),
"gal-3-28": dict(
 es="Escrito en un mundo donde esas tres distinciones lo decidían todo: derechos, tribunales, herencia. Pablo nombra justo las fronteras que no se podían cruzar.",
 fr="Écrit dans un monde où ces trois distinctions décidaient de tout : droits, tribunaux, héritage. Paul nomme précisément les frontières infranchissables.",
 de="Geschrieben in einer Welt, in der diese drei Unterschiede alles entschieden: Rechte, Gerichte, Erbe. Paulus nennt genau die Grenzen, die man nicht übertreten konnte."),
"gal-6-2": dict(
 es="Está junto a una línea que dice que cada uno llevará su propia carga. Las palabras griegas difieren: una es un peso aplastante, la otra un fardo de viaje.",
 fr="Cela voisine une ligne disant que chacun portera son propre fardeau. Les mots grecs diffèrent : l’un est un poids écrasant, l’autre un paquetage de voyage.",
 de="Es steht neben einer Zeile, dass jeder seine eigene Last trage. Die griechischen Wörter unterscheiden sich: eines meint erdrückendes Gewicht, das andere ein Reisegepäck."),
"eph-4-2": dict(
 es="Comienzo de la mitad práctica de la carta. La palabra traducida «soportándoos» significa aguantar a alguien incómodo, no perdonar una ofensa.",
 fr="Début de la moitié pratique de la lettre. Le mot rendu par « vous supportant » signifie endurer quelqu’un d’encombrant, non pardonner une offense.",
 de="Der Beginn des praktischen Briefteils. Das mit „ertragen“ übersetzte Wort meint, einen unbequemen Menschen auszuhalten, nicht eine Kränkung zu verzeihen."),
"eph-4-26": dict(
 es="Aquí no se prohíbe la ira; se le pone un plazo. La medida viene del día mismo: la puesta de sol era el fin del día, no una figura retórica.",
 fr="La colère n’est pas interdite ici ; on lui fixe un délai. La mesure vient du jour lui-même : le coucher du soleil était la fin du jour, non une image.",
 de="Zorn wird hier nicht verboten; ihm wird eine Frist gesetzt. Das Maß kommt vom Tag selbst: Sonnenuntergang war das Tagesende, keine Redewendung."),
"eph-5-15": dict(
 es="La expresión traducida «aprovechando el tiempo» significa literalmente recomprar el tiempo, como se compran mercancías, porque los días son malos.",
 fr="L’expression rendue par « rachetant le temps » signifie littéralement racheter le temps comme on achète au marché, parce que les jours sont mauvais.",
 de="Der mit „die Zeit auskaufen“ übersetzte Ausdruck meint wörtlich, Zeit zurückzukaufen wie Ware auf dem Markt, weil die Tage böse sind."),
"php-3-13": dict(
 es="Pablo acaba de enumerar su pasado, incluida la persecución de la iglesia, y llamarlo todo basura. El olvido de aquí cubre tanto sus méritos como su culpa.",
 fr="Paul vient d’énumérer son passé, y compris la persécution de l’Église, et d’appeler tout cela des ordures. L’oubli couvre ici ses titres comme sa faute.",
 de="Paulus hat gerade seine Vergangenheit aufgezählt, samt der Verfolgung der Gemeinde, und alles Dreck genannt. Das Vergessen umfasst hier Verdienste wie Schuld."),
"php-4-11": dict(
 es="Pablo subraya que aprendió a contentarse, no que empezara contento. Nombra las dos escuelas por las que pasó: la abundancia y el hambre.",
 fr="Paul souligne qu’il a appris le contentement, non qu’il a commencé content. Il nomme les deux écoles par lesquelles il est passé : l’abondance et la faim.",
 de="Paulus betont, dass er die Genügsamkeit gelernt hat, nicht dass er genügsam begann. Er nennt beide Schulen, die er durchlief: Sattsein und Hungern."),
"col-3-15": dict(
 es="El verbo traducido «reine» viene del deporte: describía al árbitro que otorgaba el premio. La paz se instala como juez dentro de la persona.",
 fr="Le verbe rendu par « règne » vient du sport : il décrivait l’arbitre attribuant le prix. La paix est installée en arbitre à l’intérieur de la personne.",
 de="Das mit „regieren“ übersetzte Verb stammt aus dem Sport: es beschrieb den Kampfrichter, der den Preis zusprach. Der Friede wird als Schiedsrichter im Menschen eingesetzt."),
"col-4-6": dict(
 es="La sal en aquel mundo era conservante y medida de valor, no un condimento para dar filo. La idea es que las palabras no se echen a perder.",
 fr="Le sel dans ce monde était un conservateur et une mesure de valeur, non un condiment mordant. L’idée est que les paroles ne se gâtent pas.",
 de="Salz war in jener Welt Konservierungsmittel und Wertmaßstab, kein Gewürz für Schärfe. Gemeint ist, dass Worte nicht verderben sollen."),
"1th-5-11": dict(
 es="Dicho a una comunidad que esperaba el fin cualquier día y estaba nerviosa por ello. La instrucción es sencilla: seguid haciendo lo que ya hacéis.",
 fr="Dit à une communauté qui attendait la fin d’un jour à l’autre et s’en inquiétait. L’instruction est simple : continuez ce que vous faites déjà.",
 de="Gesagt zu einer Gemeinde, die das Ende täglich erwartete und darüber nervös war. Die Anweisung ist schlicht: macht weiter, was ihr ohnehin tut."),
"1ti-4-12": dict(
 es="Escrito a Timoteo, dejado en Éfeso al frente de una comunidad siendo notablemente más joven que las personas a las que dirigía.",
 fr="Écrit à Timothée, laissé à Éphèse à la tête d’une communauté alors qu’il était nettement plus jeune que ceux qu’il dirigeait.",
 de="Geschrieben an Timotheus, der in Ephesus eine Gemeinde leiten sollte, obwohl er deutlich jünger war als die Menschen, die er führte."),
"1ti-6-6": dict(
 es="Dicho en una sección sobre gente que trata la piedad como modo de ganar dinero. La medida de suficiencia que se da es comida y ropa, y nada más.",
 fr="Dit dans une section sur des gens qui traitent la piété comme un moyen de gagner de l’argent. La mesure du suffisant donnée est nourriture et vêtement.",
 de="Gesagt in einem Abschnitt über Leute, die Frömmigkeit als Gelderwerb behandeln. Das genannte Maß des Genügens ist Nahrung und Kleidung, sonst nichts."),
"2ti-4-7": dict(
 es="Líneas finales de la última carta de Pablo. Unos versículos después, en el 13, pide el manto que dejó en Troas: el balance está entre encargos domésticos.",
 fr="Lignes finales de la dernière lettre de Paul. Quelques versets plus loin, au verset 13, il demande le manteau laissé à Troas : le bilan tient parmi des courses.",
 de="Die Schlusszeilen des letzten Paulusbriefes. Wenig später, in Vers 13, bittet er um den Mantel, den er in Troas ließ: die Bilanz steht zwischen Alltagsbitten."),
"heb-6-19": dict(
 es="El ancla aquí no se echa hacia abajo sino hacia arriba, tras el velo del templo. La imagen está deliberadamente invertida respecto de la náutica.",
 fr="L’ancre ici n’est pas jetée vers le bas mais vers le haut, derrière le voile du temple. L’image est délibérément inversée par rapport à la marine.",
 de="Der Anker wird hier nicht nach unten geworfen, sondern nach oben, hinter den Tempelvorhang. Das Bild ist gegenüber dem seemännischen bewusst umgekehrt."),
"heb-10-24": dict(
 es="Dicho a una comunidad donde algunos ya habían empezado a faltar a las reuniones. El verbo traducido «estimular» significa provocar, palabra bastante afilada.",
 fr="Dit à une communauté où certains avaient déjà commencé à déserter les réunions. Le verbe rendu par « stimuler » signifie provoquer, mot assez tranchant.",
 de="Gesagt zu einer Gemeinde, in der einige den Versammlungen schon fernblieben. Das mit „anspornen“ übersetzte Verb heißt reizen — ein ziemlich scharfes Wort."),
"heb-12-11": dict(
 es="El autor admite abiertamente que en el momento no parece agradable, y no intenta sostener lo contrario. Del fruto se habla en futuro.",
 fr="L’auteur admet ouvertement que sur le moment cela ne paraît pas agréable, et n’essaie pas de soutenir le contraire. Le fruit est évoqué au futur.",
 de="Der Verfasser gibt offen zu, dass es im Augenblick nicht angenehm scheint, und behauptet nichts anderes. Von der Frucht spricht er im Futur."),
"jas-1-17": dict(
 es="Imagen astronómica: los cuerpos celestes tienen fases y eclipses, y Santiago dice que aquí no los hay. La comparación es más precisa de lo que suena.",
 fr="Image astronomique : les corps célestes ont des phases et des éclipses, et Jacques dit qu’ici il n’y en a pas. La comparaison est plus précise qu’il n’y paraît.",
 de="Ein astronomisches Bild: Himmelskörper haben Phasen und Finsternisse, und Jakobus sagt, hier gebe es keine. Der Vergleich ist genauer, als er klingt."),
"jas-1-19": dict(
 es="Tres instrucciones en orden de dificultad. Santiago escribe a una comunidad donde, a juzgar por la carta, se discutía con frecuencia y entusiasmo.",
 fr="Trois instructions par ordre de difficulté. Jacques écrit à une communauté où, à en juger par la lettre, on discutait souvent et avec entrain.",
 de="Drei Anweisungen in der Reihenfolge ihrer Schwierigkeit. Jakobus schreibt an eine Gemeinde, in der dem Brief nach häufig und begeistert gestritten wurde."),
"jas-4-14": dict(
 es="Dicho sobre gente que planeaba un año de viajes y ganancias por delante. Santiago no prohíbe planear; objeta a la certeza sobre el mañana.",
 fr="Dit à propos de gens qui planifiaient une année de voyages et de profits. Jacques n’interdit pas de planifier ; il conteste la certitude sur le lendemain.",
 de="Gesagt über Leute, die ein Jahr voller Reisen und Gewinne planten. Jakobus verbietet das Planen nicht; er wendet sich gegen die Gewissheit über morgen."),
"1pe-1-3": dict(
 es="Comienzo de una carta a cristianos llamados forasteros en sus propias ciudades. La esperanza se llama viva, por contraste con una herencia que puede perderse.",
 fr="Ouverture d’une lettre à des chrétiens appelés étrangers dans leurs propres villes. L’espérance est dite vivante, par contraste avec un héritage qui peut se perdre.",
 de="Der Anfang eines Briefes an Christen, die in ihren eigenen Städten Fremde hießen. Die Hoffnung wird lebendig genannt, im Gegensatz zu einem verlierbaren Erbe."),
"1pe-3-15": dict(
 es="Dicho a gente a la que podían llamar a interrogatorio. La exigencia de dar respuesta viene junto con la de hacerlo con mansedumbre, no con triunfo.",
 fr="Dit à des gens susceptibles d’être convoqués pour interrogatoire. L’exigence de répondre va de pair avec celle de le faire avec douceur, non en triomphant.",
 de="Gesagt zu Menschen, die zum Verhör geladen werden konnten. Die Forderung zu antworten steht zusammen mit der, es sanftmütig zu tun, nicht triumphierend."),
"1pe-5-10": dict(
 es="Pedro escribe «después de que hayáis padecido un poco», sin prometer que no habrá sufrimiento. El «poco» es su propia estimación, desde dentro de la persecución.",
 fr="Pierre écrit « après que vous aurez souffert un peu », sans promettre l’absence de souffrance. Ce « peu » est sa propre estimation, de l’intérieur de la persécution.",
 de="Petrus schreibt „nachdem ihr eine kleine Zeit gelitten habt“, ohne Leidensfreiheit zu versprechen. Das „klein“ ist seine eigene Einschätzung, mitten in der Verfolgung."),
"2pe-3-9": dict(
 es="Respuesta a quienes preguntaban dónde está la venida prometida, ya que nada ocurre. La demora no se explica por olvido, sino por intención.",
 fr="Réponse à ceux qui demandaient où est la venue promise, puisque rien n’arrive. Le retard n’est pas expliqué par l’oubli mais par une intention.",
 de="Die Antwort an jene, die fragten, wo die verheißene Ankunft bleibe, da nichts geschehe. Die Verzögerung wird nicht mit Vergesslichkeit erklärt, sondern mit Absicht."),
"1jn-3-1": dict(
 es="El verbo con que se abre la línea es una exclamación: «mirad». Juan escribe a una comunidad de la que algunos se habían ido, y explica a los que quedaron quiénes son.",
 fr="Le verbe qui ouvre la ligne est une exclamation : « voyez ». Jean écrit à une communauté que certains ont quittée, et explique à ceux qui restent qui ils sont.",
 de="Das Verb am Zeilenanfang ist ein Ausruf: „seht“. Johannes schreibt an eine Gemeinde, die einige verlassen haben, und erklärt den Gebliebenen, wer sie sind."),
"1jn-3-18": dict(
 es="Justo antes está la pregunta sobre quien ve a un hermano en necesidad y le cierra el corazón. La exigencia de obrar llega como respuesta a esa pregunta.",
 fr="Juste avant se tient la question sur celui qui voit un frère dans le besoin et lui ferme son cœur. L’exigence d’agir vient en réponse à cette question.",
 de="Direkt davor steht die Frage nach dem, der einen Bruder in Not sieht und sein Herz verschließt. Die Forderung zu handeln kommt als Antwort darauf."),
"1jn-4-19": dict(
 es="Línea breve sobre el orden: el nuestro no es el primero. Está inmediatamente después de las palabras sobre el miedo expulsado por el amor.",
 fr="Ligne brève sur l’ordre : le nôtre n’est pas premier. Elle suit immédiatement les mots sur la peur chassée par l’amour.",
 de="Eine kurze Zeile über die Reihenfolge: unsere ist nicht die erste. Sie steht unmittelbar nach den Worten über die von der Liebe ausgetriebene Furcht."),
"rev-2-10": dict(
 es="Carta a la iglesia de Esmirna, una de las dos, junto con Filadelfia, que no reciben ningún reproche. Lo que se les promete no es rescate, sino cárcel y diez días de aflicción.",
 fr="Lettre à l’Église de Smyrne, l’une des deux, avec Philadelphie, qui ne reçoivent aucun reproche. Ce qui leur est promis n’est pas le secours, mais la prison et dix jours d’affliction.",
 de="Ein Brief an die Gemeinde in Smyrna, neben Philadelphia die einzige, der nichts vorgeworfen wird. Verheißen wird ihnen keine Rettung, sondern Gefängnis und zehn Tage Bedrängnis."),
"rev-21-5": dict(
 es="Una de las pocas líneas del libro dichas directamente por el que está en el trono. Lo prometido no son cosas nuevas, sino la renovación de todo lo que existe.",
 fr="L’une des rares lignes du livre prononcées directement par celui qui est sur le trône. Ce qui est promis n’est pas du neuf, mais le renouvellement de tout.",
 de="Eine der wenigen Zeilen des Buches, die der auf dem Thron unmittelbar spricht. Verheißen werden nicht neue Dinge, sondern die Erneuerung von allem Bestehenden."),
"gen-4-9": dict(
 es="Caín responde a una pregunta con otra, habiendo ya matado a su hermano. Su contrapregunta —si es guardián de su hermano— nunca recibe respuesta directa.",
 fr="Caïn répond à une question par une question, ayant déjà tué son frère. Sa contre-question — suis-je le gardien de mon frère — ne reçoit jamais de réponse.",
 de="Kain antwortet auf eine Frage mit einer Frage, nachdem er seinen Bruder bereits erschlagen hat. Seine Gegenfrage bleibt in der Bibel unbeantwortet."),
"gen-18-14": dict(
 es="Dicho después de que Sara se riera tras la pared de la tienda al oír lo del hijo. Tiene noventa años, y se rió por dentro, no en voz alta.",
 fr="Dit après que Sara eut ri derrière la paroi de la tente en entendant parler d’un fils. Elle a quatre-vingt-dix ans, et elle a ri en dedans, non tout haut.",
 de="Gesagt, nachdem Sara hinter der Zeltwand lachte, als sie von einem Sohn hörte. Sie ist neunzig, und sie lachte innerlich, nicht laut."),
"exo-4-11": dict(
 es="Respuesta a Moisés, que había rehusado cuatro veces alegando ser torpe de lengua. Después de esto rehúsa una quinta vez.",
 fr="Réponse à Moïse, qui avait refusé quatre fois en plaidant qu’il avait la langue lourde. Après cela, il refuse une cinquième fois.",
 de="Die Antwort an Mose, der viermal abgelehnt und eingewandt hatte, er sei schwer von Zunge. Danach lehnt er ein fünftes Mal ab."),
"exo-17-12": dict(
 es="Mientras Moisés mantenía las manos alzadas la batalla iba a favor de Israel, pero sus manos pesaban. Aarón y Hur le pusieron una piedra y le sostuvieron los brazos.",
 fr="Tant que Moïse gardait les mains levées la bataille tournait pour Israël, mais ses mains s’alourdissaient. Aaron et Hour lui mirent une pierre et soutinrent ses bras.",
 de="Solange Mose die Hände erhoben hielt, ging die Schlacht für Israel, doch seine Hände wurden schwer. Aaron und Hur schoben ihm einen Stein unter und stützten die Arme."),
"num-11-14": dict(
 es="Moisés dice esto mientras el pueblo llora pidiendo carne. Luego pide sin rodeos que lo maten si aquello sigue, y eso queda registrado sin suavizarlo.",
 fr="Moïse dit cela pendant que le peuple pleure pour de la viande. Il demande ensuite franchement qu’on le tue si cela continue, et c’est noté sans adoucissement.",
 de="Mose sagt das, während das Volk um Fleisch weint. Danach bittet er unumwunden, getötet zu werden, wenn es so weitergeht — und das steht ungeschönt da."),
"deu-4-29": dict(
 es="Dicho para el caso en que el pueblo ya esté disperso entre otras naciones. La promesa se da por adelantado, para el peor desenlace previsto.",
 fr="Dit pour le cas où le peuple sera déjà dispersé parmi d’autres nations. La promesse est donnée d’avance, pour l’issue la pire envisagée.",
 de="Gesagt für den Fall, dass das Volk bereits unter andere Nationen zerstreut ist. Die Zusage wird im Voraus gegeben, für den schlimmsten erwarteten Ausgang."),
"jos-14-11": dict(
 es="Dicho por Caleb a los ochenta y cinco años, pidiendo no una parcela tranquila sino la región montañosa donde viven los gigantes.",
 fr="Dit par Caleb à quatre-vingt-cinq ans, demandant non un lot tranquille mais la montagne où vivent les géants.",
 de="Gesagt von Kaleb mit fünfundachtzig Jahren, der nicht um ein ruhiges Stück Land bittet, sondern um das Bergland, in dem die Riesen wohnen."),
"jdg-16-28": dict(
 es="Última oración de Sansón: ciego, rapado y exhibido para la burla. Antes, el libro solo recoge una oración suya, cuando se moría de sed.",
 fr="Dernière prière de Samson : aveugle, tondu et exposé à la moquerie. Auparavant, le livre ne rapporte qu’une seule prière de lui, quand il mourait de soif.",
 de="Simsons letztes Gebet — geblendet, geschoren und zum Spott vorgeführt. Davor berichtet das Buch nur ein einziges Gebet von ihm, als er fast verdurstete."),
"1sa-1-15": dict(
 es="Ana se defiende ante un sacerdote que la tomó por borracha: oraba en silencio, moviendo solo los labios. Entonces no se rezaba así.",
 fr="Anne se défend devant un prêtre qui l’a prise pour une ivrogne : elle priait en silence, seules ses lèvres bougeaient. On ne priait pas ainsi alors.",
 de="Hanna verteidigt sich vor einem Priester, der sie für betrunken hielt: sie betete lautlos, nur die Lippen bewegten sich. So betete man damals nicht."),
"1sa-7-12": dict(
 es="Samuel levanta una piedra y la llama «piedra de ayuda». El mojón no se pone tras una victoria en general, sino en un punto concreto.",
 fr="Samuel dresse une pierre et la nomme « pierre du secours ». Le repère n’est pas posé après une victoire en général, mais à un endroit précis.",
 de="Samuel richtet einen Stein auf und nennt ihn „Stein der Hilfe“. Das Mal wird nicht nach einem Sieg allgemein gesetzt, sondern an einer bestimmten Stelle."),
"2sa-9-7": dict(
 es="David dice esto al nieto de Saúl, el hombre que lo persiguió durante años. Mefiboset está cojo de ambos pies y vive en casa ajena.",
 fr="David dit cela au petit-fils de Saül, l’homme qui l’a traqué des années. Mephibosheth est boiteux des deux pieds et vit chez autrui.",
 de="David sagt das zum Enkel Sauls, des Mannes, der ihn jahrelang jagte. Mefi-Boschet ist an beiden Füßen gelähmt und lebt im Haus eines anderen."),
"1ki-3-9": dict(
 es="A Salomón le ofrecen lo que pida, y no pide riqueza ni larga vida, sino la capacidad de distinguir. Tenía unos veinte años.",
 fr="On offre à Salomon ce qu’il veut, et il ne demande ni richesse ni longue vie, mais la capacité de discerner. Il avait environ vingt ans.",
 de="Salomo darf sich erbitten, was er will, und bittet nicht um Reichtum oder langes Leben, sondern um die Fähigkeit zu unterscheiden. Er war etwa zwanzig."),
"1ki-17-16": dict(
 es="La viuda de Sarepta preparaba un último pan para ella y su hijo, para comerlo y morir. La harina y el aceite no se acabaron hasta el fin de la sequía.",
 fr="La veuve de Sarepta préparait un dernier pain pour elle et son fils, pour le manger et mourir. La farine et l’huile ne manquèrent pas jusqu’à la fin de la sécheresse.",
 de="Die Witwe von Sarepta backte ein letztes Brot für sich und ihren Sohn, um es zu essen und zu sterben. Mehl und Öl gingen bis zum Ende der Dürre nicht aus."),
"1ki-19-4": dict(
 es="Elías pide morir bajo un arbusto en el desierto, al día siguiente de la mayor victoria de su vida. La respuesta que recibe es comida y sueño.",
 fr="Élie demande à mourir sous un buisson au désert, le lendemain de la plus grande victoire de sa vie. La réponse qu’il reçoit est nourriture et sommeil.",
 de="Elia bittet unter einem Strauch in der Wüste zu sterben, am Tag nach dem größten Sieg seines Lebens. Die Antwort, die er bekommt, sind Essen und Schlaf."),

# ── партия 4 ──────────────────────────────────────────────────────────────
"2ki-4-26": dict(
 es="La mujer responde «todo va bien», aunque su hijo único murió esa mañana en sus brazos. No se lo dijo a nadie hasta llegar al profeta.",
 fr="La femme répond « tout va bien », alors que son fils unique est mort ce matin-là dans ses bras. Elle ne l’a dit à personne avant d’atteindre le prophète.",
 de="Die Frau antwortet „es ist gut“, obwohl ihr einziger Sohn an jenem Morgen in ihren Armen starb. Sie sagte es niemandem, bis sie den Propheten erreichte."),
"1ch-28-20": dict(
 es="David entrega a Salomón los planos de un templo que a él no le dejaron construir. Se lo dice a su hijo sabiendo que no verá la obra.",
 fr="David remet à Salomon les plans d’un temple qu’on ne lui a pas laissé bâtir. Il le dit à son fils en sachant qu’il ne verra pas l’ouvrage.",
 de="David übergibt Salomo die Pläne für einen Tempel, den er selbst nicht bauen durfte. Er sagt es seinem Sohn im Wissen, dass er das Werk nicht sehen wird."),
"2ch-16-9": dict(
 es="Dicho al rey Asá como reproche: contrató a un aliado en vez de apoyarse en Dios, y se le acusa no de fracaso sino de cálculo.",
 fr="Dit au roi Asa en reproche : il a loué un allié au lieu de s’appuyer sur Dieu, et on lui reproche non un échec mais un calcul.",
 de="Gesagt zu König Asa als Vorwurf: er warb einen Verbündeten an, statt sich auf Gott zu stützen, und wird nicht des Scheiterns, sondern des Kalküls beschuldigt."),
"neh-1-4": dict(
 es="Nehemías es copero del rey persa y acaba de oír que las murallas de Jerusalén están en ruinas. Lloró y ayunó días antes de hacer nada.",
 fr="Néhémie est échanson du roi de Perse et vient d’apprendre que les murailles de Jérusalem sont en ruines. Il pleura et jeûna des jours avant d’agir.",
 de="Nehemia ist Mundschenk des Perserkönigs und hat eben gehört, dass Jerusalems Mauern in Trümmern liegen. Er weinte und fastete tagelang, bevor er etwas tat."),
"est-4-16": dict(
 es="Ester decide presentarse ante el rey sin ser llamada, conociendo la ley. Sus últimas palabras —si perezco, que perezca— no son esperanza sino aceptación.",
 fr="Esther décide de se présenter au roi sans être appelée, connaissant la loi. Ses derniers mots — si je péris, je péris — ne sont pas l’espoir mais l’acceptation.",
 de="Ester beschließt, ungerufen vor den König zu treten, obwohl sie das Gesetz kennt. Ihre letzten Worte — komme ich um, so komme ich um — sind Einwilligung, nicht Hoffnung."),
"job-2-10": dict(
 es="Respuesta a su mujer, que le sugirió maldecir a Dios y morir. Job en ese momento está sentado en ceniza, rascándose con un pedazo de barro cocido.",
 fr="Réponse à sa femme, qui lui suggérait de maudire Dieu et de mourir. Job à cet instant est assis dans la cendre, se grattant avec un tesson.",
 de="Die Antwort an seine Frau, die ihm riet, Gott zu verfluchen und zu sterben. Hiob sitzt in diesem Moment in der Asche und schabt sich mit einer Scherbe."),
"job-14-1": dict(
 es="Job habla de la vida humana en general, en medio de una discusión sobre la suya. Las imágenes vienen de la naturaleza: una flor y una sombra, ambas breves.",
 fr="Job parle de la vie humaine en général, au milieu d’une dispute sur la sienne. Les images viennent de la nature : une fleur et une ombre, toutes deux brèves.",
 de="Hiob spricht vom menschlichen Leben allgemein, mitten in einem Streit über sein eigenes. Die Bilder stammen aus der Natur: eine Blume und ein Schatten, beide kurz."),
"job-29-2": dict(
 es="Job recuerda cómo eran antes las cosas, en el único capítulo del libro dedicado por entero a añorar el pasado. No pide que vuelva; lo enumera.",
 fr="Job se souvient de ce qui était, dans le seul chapitre du livre entièrement voué à la nostalgie du passé. Il ne demande pas son retour ; il l’énumère.",
 de="Hiob erinnert sich, wie es früher war, im einzigen Kapitel des Buches, das ganz der Sehnsucht nach der Vergangenheit gilt. Er fordert sie nicht zurück, er zählt auf."),
"psa-5-3": dict(
 es="Salmo matutino de David. El verbo traducido «presentar» viene del culto sacrificial: describía la colocación de la leña al amanecer.",
 fr="Psaume du matin de David. Le verbe rendu par « présenter » vient du culte sacrificiel : il décrivait la disposition du bois à l’aube.",
 de="Ein Morgenpsalm Davids. Das mit „darlegen“ übersetzte Verb stammt aus dem Opferdienst: es beschrieb das Schichten des Holzes bei Tagesanbruch."),
"psa-6-6": dict(
 es="David escribe que se agota gimiendo toda la noche y empapa su lecho de lágrimas. El salmo se clasifica como penitencial, pero su queja es corporal.",
 fr="David écrit qu’il s’épuise à gémir toute la nuit et trempe son lit de larmes. Le psaume est classé pénitentiel, mais sa plainte est corporelle.",
 de="David schreibt, er erschöpfe sich die Nacht hindurch im Stöhnen und tränke sein Bett mit Tränen. Der Psalm gilt als Bußpsalm, doch seine Klage ist leiblich."),
"psa-9-9": dict(
 es="La palabra traducida «refugio» significa una altura a la que no se llega desde abajo. Este salmo y el siguiente forman juntos un solo acróstico; la Biblia griega los cuenta como uno.",
 fr="Le mot rendu par « refuge » désigne une hauteur inaccessible d’en bas. Ce psaume et le suivant forment ensemble un seul acrostiche ; la Bible grecque les compte comme un seul psaume.",
 de="Das mit „Schutz“ übersetzte Wort meint eine Höhe, die von unten unerreichbar ist. Dieser und der nächste Psalm bilden zusammen ein Akrostichon; die griechische Bibel zählt sie als einen."),
"psa-17-8": dict(
 es="Dos imágenes seguidas: la pupila del ojo, protegida sin pensarlo, y un ave que recoge sus polluelos bajo el ala. Ambas vienen del reflejo, no de la elección.",
 fr="Deux images à la suite : la pupille de l’œil, protégée sans y penser, et un oiseau abritant ses petits sous l’aile. Toutes deux viennent du réflexe, non du choix.",
 de="Zwei Bilder hintereinander: die Pupille des Auges, ohne Nachdenken geschützt, und ein Vogel, der seine Jungen unter den Flügel nimmt. Beide sind Reflex, nicht Wahl."),
"psa-18-28": dict(
 es="El salmo se escribió el día en que David escapó de Saúl. La lámpara de aquí es el mismo candil de barro que da nombre a la aplicación.",
 fr="Le psaume fut écrit le jour où David échappa à Saül. La lampe dont il s’agit est la même petite lampe d’argile qui donne son nom à l’application.",
 de="Der Psalm entstand an dem Tag, als David Saul entkam. Die Leuchte hier ist dieselbe kleine Tonlampe, nach der die App benannt ist."),
"psa-24-1": dict(
 es="Salmo para entrar en el templo, cantado en las puertas. La afirmación de que toda la tierra es de Dios se decía justo antes de pisar una parcela pequeña.",
 fr="Psaume pour entrer au temple, chanté aux portes. L’affirmation que toute la terre est à Dieu était dite juste avant de poser le pied sur un petit lopin.",
 de="Ein Psalm für den Eintritt in den Tempel, an den Toren gesungen. Die Aussage, die ganze Erde gehöre Gott, fiel unmittelbar vor dem Betreten eines kleinen Grundstücks."),
"psa-41-1": dict(
 es="Salmo de un enfermo que escribe que las visitas vienen y le mienten a la cara. La línea sobre cuidar del pobre está al principio, antes de la queja.",
 fr="Psaume d’un malade qui écrit que les visiteurs viennent et lui mentent en face. La ligne sur le souci du pauvre est au début, avant la plainte.",
 de="Der Psalm eines Kranken, der schreibt, Besucher kämen und belögen ihn ins Gesicht. Die Zeile über die Sorge um den Armen steht am Anfang, vor der Klage."),
"psa-50-15": dict(
 es="Salmo donde Dios rechaza los sacrificios explicando que no tiene hambre. En lugar de carne pide acción de gracias y que se le llame en la angustia.",
 fr="Psaume où Dieu refuse les sacrifices en expliquant qu’il n’a pas faim. Au lieu de viande, il demande l’action de grâce et qu’on l’appelle dans la détresse.",
 de="Ein Psalm, in dem Gott Opfer ablehnt und erklärt, er sei nicht hungrig. Statt Fleisch verlangt er Dank und den Anruf in der Not."),
"psa-57-1": dict(
 es="El encabezado sitúa este salmo cuando David se escondía de Saúl en una cueva. La sombra de las alas es una imagen de ave, no de arquitectura.",
 fr="Le titre situe ce psaume quand David se cachait de Saül dans une grotte. L’ombre des ailes est une image d’oiseau, non d’architecture.",
 de="Die Überschrift verortet diesen Psalm in der Zeit, als David sich vor Saul in einer Höhle verbarg. Der Schatten der Flügel ist ein Vogelbild, kein bauliches."),
"psa-70-5": dict(
 es="Salmo breve hecho enteramente de una petición de darse prisa. Las últimas palabras en hebreo son «no tardes», y ahí se corta.",
 fr="Bref psaume fait entièrement d’une demande de se hâter. Les derniers mots en hébreu sont « ne tarde pas », et il s’arrête là.",
 de="Ein kurzer Psalm, der ganz aus der Bitte um Eile besteht. Die letzten Worte lauten hebräisch „säume nicht“, und dort bricht er ab."),
"psa-78-4": dict(
 es="Comienzo del salmo histórico más largo. Después relata con honradez también los fracasos del pueblo: la tarea es transmitir, no mejorar lo ocurrido.",
 fr="Début du plus long psaume historique. Il raconte ensuite honnêtement aussi les échecs du peuple : la tâche est de transmettre, non d’embellir.",
 de="Der Anfang des längsten Geschichtspsalms. Er erzählt danach ehrlich auch das Versagen des Volkes: die Aufgabe ist weiterzugeben, nicht zu beschönigen."),
"psa-82-3": dict(
 es="Salmo que acusa a los jueces de juzgar sin justicia y favorecer a los poderosos. La exigencia va dirigida a quienes tienen poder para decidir.",
 fr="Psaume qui accuse les juges de juger injustement et de favoriser les puissants. L’exigence s’adresse à ceux qui ont le pouvoir de décider.",
 de="Ein Psalm, der Richter beschuldigt, ungerecht zu urteilen und die Mächtigen zu bevorzugen. Die Forderung richtet sich an die, die Entscheidungsmacht haben."),
"psa-84-5": dict(
 es="Salmo de peregrino. El hebreo habla de gente que lleva los caminos en el corazón: atraviesan un valle de lágrimas y lo convierten en manantial.",
 fr="Psaume de pèlerin. L’hébreu parle de gens qui ont les chemins dans le cœur : ils traversent une vallée de larmes et la changent en source.",
 de="Ein Pilgerpsalm. Der hebräische Text spricht von Menschen, die die Wege im Herzen tragen: sie durchziehen ein Tal der Tränen und machen es zur Quelle."),
"psa-92-14": dict(
 es="Salmo para el sábado. Imagen botánica: las palmeras datileras y los cedros dan más cuanto más viejos son, y todo oyente lo sabía.",
 fr="Psaume pour le sabbat. Image botanique : les palmiers-dattiers et les cèdres portent davantage en vieillissant, et tout auditeur le savait.",
 de="Ein Psalm für den Sabbat. Ein botanisches Bild: Dattelpalmen und Zedern tragen mehr, je älter sie werden, und jeder Zuhörer wusste das."),
"psa-115-1": dict(
 es="Salmo del ciclo pascual que se abre rechazando el mérito. Después se burla de los ídolos que tienen ojos y oídos que no funcionan.",
 fr="Psaume du cycle pascal qui s’ouvre en refusant le mérite. Il raille ensuite les idoles qui ont des yeux et des oreilles qui ne servent à rien.",
 de="Ein Psalm aus dem Passazyklus, der mit der Ablehnung des eigenen Verdienstes beginnt. Danach verspottet er Götzen mit Augen und Ohren, die nicht funktionieren."),
"psa-117-1": dict(
 es="El salmo más corto del Salterio, de dos líneas. Aun así se dirige a todas las naciones y no a Israel, lo cual es raro en el Salterio.",
 fr="Le plus court psaume du Psautier, de deux lignes. Il s’adresse pourtant à toutes les nations et non à Israël, ce qui est rare dans le Psautier.",
 de="Der kürzeste Psalm des Psalters, zwei Zeilen lang. Dennoch wendet er sich an alle Völker statt an Israel, was im Psalter selten ist."),
"psa-119-130": dict(
 es="Del salmo más largo, un acróstico sobre la ley. El verbo traducido «revelación» significa literalmente apertura: como se abre una puerta y entra la luz.",
 fr="Du plus long des psaumes, un acrostiche sur la loi. Le verbe rendu par « révélation » signifie littéralement ouverture : on ouvre une porte et la lumière entre.",
 de="Aus dem längsten Psalm, einem Akrostichon über das Gesetz. Das mit „Offenbarung“ übersetzte Wort meint wörtlich ein Öffnen: eine Tür geht auf, Licht fällt herein."),
"psa-150-6": dict(
 es="Línea final de todo el Salterio, tras ciento cuarenta y nueve salmos que incluían maldiciones y quejas por el silencio de Dios.",
 fr="Dernière ligne de tout le Psautier, après cent quarante-neuf psaumes comprenant des malédictions et des plaintes sur le silence de Dieu.",
 de="Die Schlusszeile des ganzen Psalters, nach hundertneunundvierzig Psalmen, die Flüche und Klagen über Gottes Schweigen enthielten."),
"pro-6-6": dict(
 es="El consejo de mirar a la hormiga se da a un perezoso. El argumento se apoya en que la hormiga no tiene jefe ni capataz, y el trabajo se hace igual.",
 fr="Le conseil de regarder la fourmi s’adresse à un paresseux. L’argument tient à ce que la fourmi n’a ni chef ni surveillant, et que le travail se fait quand même.",
 de="Der Rat, die Ameise anzusehen, gilt einem Faulen. Das Argument stützt sich darauf, dass die Ameise weder Anführer noch Aufseher hat und die Arbeit dennoch geschieht."),
"pro-13-12": dict(
 es="Dicho sobre lo que la espera aplazada le hace físicamente a una persona. Ambas imágenes son corporales: un corazón enfermo y un árbol de vida.",
 fr="Sentence sur ce que l’attente différée fait physiquement à une personne. Les deux images sont corporelles : un cœur malade et un arbre de vie.",
 de="Ein Spruch darüber, was aufgeschobenes Warten körperlich mit einem Menschen macht. Beide Bilder sind leiblich: ein krankes Herz und ein Baum des Lebens."),
"pro-17-17": dict(
 es="El dicho distingue al amigo del hermano: el primero ama en todo tiempo, el segundo es para la desgracia. No son sinónimos, sino dos casos distintos.",
 fr="La sentence distingue l’ami du frère : le premier aime en tout temps, le second est pour le malheur. Ce ne sont pas des synonymes mais deux cas différents.",
 de="Der Spruch unterscheidet Freund und Bruder: der eine liebt allezeit, der andere ist für die Not da. Es sind keine Synonyme, sondern zwei verschiedene Fälle."),
"pro-25-11": dict(
 es="De una colección reunida por los hombres del rey Ezequías. Imagen de joyero: fruta de oro en engaste de plata, algo caro y hecho justo a medida.",
 fr="D’un recueil rassemblé par les hommes du roi Ézéchias. Image de joaillier : un fruit d’or dans une monture d’argent, objet coûteux fait exactement sur mesure.",
 de="Aus einer Sammlung, die Männer des Königs Hiskia zusammentrugen. Ein Goldschmiedebild: goldene Frucht in silberner Fassung, teuer und genau nach Maß gefertigt."),
"pro-28-13": dict(
 es="Dicho sobre dos modos de tratar la culpa: taparla o nombrarla. El verbo «encubre» es el mismo que usa el Génesis para Adán escondiéndose.",
 fr="Sentence sur deux façons de traiter la faute : la couvrir ou la nommer. Le verbe « couvre » est celui-là même que la Genèse emploie pour Adam qui se cache.",
 de="Ein Spruch über zwei Weisen, mit Schuld umzugehen: sie zudecken oder sie benennen. Das Verb „zudecken“ ist dasselbe, das die Genesis für Adams Verstecken nutzt."),
"pro-30-8": dict(
 es="Oración rara en un libro de dichos. El autor no pide pobreza ni riqueza y explica ambos riesgos: olvidar cuando se está lleno, robar cuando falta.",
 fr="Prière rare dans un livre de sentences. L’auteur ne demande ni pauvreté ni richesse et explique les deux risques : oublier quand on est rassasié, voler quand on manque.",
 de="Ein seltenes Gebet in einem Spruchbuch. Der Verfasser bittet weder um Armut noch um Reichtum und nennt beide Gefahren: Vergessen im Überfluss, Stehlen im Mangel."),
"ecc-7-3": dict(
 es="El autor aconseja ir a una casa de duelo antes que a una de banquete. Su razón es práctica: allí se ve cómo termina la cosa para todos.",
 fr="L’auteur conseille d’aller dans une maison de deuil plutôt que dans une maison de festin. Sa raison est pratique : on y voit comment cela finit pour tous.",
 de="Der Verfasser rät, eher in ein Trauerhaus zu gehen als in ein Festhaus. Sein Grund ist praktisch: dort sieht man, wie es für jeden endet."),
"sng-2-11": dict(
 es="Invitación a salir después del invierno, de un libro sobre dos amantes. En aquella tierra las lluvias caían en invierno, y su fin terminaba el encierro.",
 fr="Invitation à sortir après l’hiver, dans un livre sur deux amants. Dans ce pays les pluies venaient en hiver, et leur fin mettait fin au confinement.",
 de="Eine Einladung, nach dem Winter hinauszugehen, aus einem Buch über zwei Liebende. Dort fielen die Regen im Winter, und ihr Ende beendete das Drinnenbleiben."),
"isa-45-3": dict(
 es="Dicho sobre Ciro, un rey persa que no conocía al Dios de Israel. La promesa de tesoros en la oscuridad se hace a un extraño, no a uno de los suyos.",
 fr="Dit à propos de Cyrus, un roi perse qui ne connaissait pas le Dieu d’Israël. La promesse de trésors dans les ténèbres est faite à un étranger, non à un des leurs.",
 de="Gesagt über Kyros, einen persischen König, der den Gott Israels nicht kannte. Die Zusage von Schätzen im Dunkeln gilt einem Fremden, nicht einem der Eigenen."),
"isa-60-1": dict(
 es="Dirigido a una ciudad en ruinas. La orden de levantarse y brillar se da a quien no tiene luz propia; la fuente se nombra en la línea siguiente.",
 fr="Adressé à une ville en ruines. L’ordre de se lever et de briller est donné à qui n’a pas de lumière propre ; la source est nommée à la ligne suivante.",
 de="An eine Stadt in Trümmern gerichtet. Der Befehl aufzustehen und zu leuchten gilt einer, die kein eigenes Licht hat; die Quelle nennt die nächste Zeile."),
"isa-64-8": dict(
 es="Línea de una oración colectiva de arrepentimiento donde el pueblo admite haberse marchitado como una hoja. La imagen del barro subraya dependencia, no humildad.",
 fr="Ligne d’une prière collective de repentance où le peuple admet s’être flétri comme une feuille. L’image de l’argile souligne la dépendance, non l’humilité.",
 de="Eine Zeile aus einem gemeinsamen Bußgebet, in dem das Volk zugibt, wie ein Blatt verwelkt zu sein. Das Tonbild betont Abhängigkeit, nicht Demut."),
"isa-66-13": dict(
 es="Último capítulo del libro. Una comparación materna es rara en los profetas, y llega justo al final, tras sesenta y cinco capítulos en otro registro.",
 fr="Dernier chapitre du livre. Une comparaison maternelle est rare chez les prophètes, et elle vient tout à la fin, après soixante-cinq chapitres d’un autre registre.",
 de="Das letzte Kapitel des Buches. Ein mütterlicher Vergleich ist bei den Propheten selten und kommt ganz am Ende, nach fünfundsechzig Kapiteln anderer Tonlage."),
"jer-2-13": dict(
 es="El profeta nombra dos males seguidos; el segundo son cisternas que no retienen agua. En un país sin ríos era el error más caro y más irritante.",
 fr="Le prophète nomme deux maux à la suite, le second étant des citernes qui ne retiennent pas l’eau. Dans un pays sans rivières, c’était l’erreur la plus coûteuse.",
 de="Der Prophet nennt zwei Übel nacheinander, das zweite sind Zisternen, die kein Wasser halten. In einem Land ohne Flüsse war das der teuerste und ärgerlichste Fehler."),
"jer-8-22": dict(
 es="El bálsamo de Galaad era un remedio conocido que llevaban las caravanas. La pregunta es retórica y amarga: la medicina existe, la curación no.",
 fr="Le baume de Galaad était un remède connu que transportaient les caravanes. La question est rhétorique et amère : le remède existe, la guérison non.",
 de="Der Balsam aus Gilead war eine bekannte Arznei, die Karawanen mitführten. Die Frage ist rhetorisch und bitter: das Heilmittel gibt es, die Heilung nicht."),
"jer-18-6": dict(
 es="A Jeremías lo mandan a un taller a mirar trabajar a alguien. La vasija salió mal en manos del alfarero, y él hizo otra del mismo barro: esa es toda la lección.",
 fr="Jérémie est envoyé dans un atelier regarder quelqu’un travailler. Le vase a raté entre les mains du potier, et il en a fait un autre de la même argile.",
 de="Jeremia wird in eine Werkstatt geschickt, um jemandem bei der Arbeit zuzusehen. Der Topf misslang unter den Händen des Töpfers, und er machte einen neuen daraus."),
"jer-20-9": dict(
 es="Jeremías acaba de pasar una noche en el cepo y ha declarado que no profetizará más. Esta es su confesión de por qué callar no funcionó.",
 fr="Jérémie vient de passer une nuit aux ceps et a déclaré qu’il ne prophétiserait plus. Voici son aveu de la raison pour laquelle se taire n’a pas marché.",
 de="Jeremia hat eben eine Nacht im Block verbracht und erklärt, er werde nicht mehr weissagen. Das ist sein Eingeständnis, warum das Schweigen nicht gelang."),
"jer-31-25": dict(
 es="Tras esta línea el profeta añade que despertó y su sueño le había sido dulce. Es el único lugar del libro donde menciona su propio sueño.",
 fr="Après cette ligne, le prophète ajoute qu’il s’est réveillé et que son sommeil lui avait été doux. C’est le seul endroit du livre où il mentionne son sommeil.",
 de="Nach dieser Zeile fügt der Prophet hinzu, er sei erwacht und sein Schlaf sei ihm süß gewesen. Es ist die einzige Stelle des Buches, an der er seinen Schlaf erwähnt."),
"lam-3-31": dict(
 es="Del lamento por Jerusalén destruida. Dice que Dios no aflige a los hombres de corazón, es decir, no de buena gana.",
 fr="Du chant de deuil sur Jérusalem détruite. Il est dit que Dieu n’afflige pas de bon cœur les humains — autrement dit, pas volontiers.",
 de="Aus der Klage über das zerstörte Jerusalem. Es heißt, Gott plage die Menschen nicht von Herzen — das heißt: nicht gern."),
"ezk-22-30": dict(
 es="Dios dice que buscó a alguien que se pusiera en la brecha del muro y no lo encontró. La línea termina con la búsqueda fracasada.",
 fr="Dieu dit qu’il a cherché quelqu’un pour se tenir sur la brèche du mur et n’a trouvé personne. La ligne s’achève sur la recherche échouée.",
 de="Gott sagt, er habe jemanden gesucht, der in die Bresche der Mauer tritt, und keinen gefunden. Die Zeile endet mit der gescheiterten Suche."),
"dan-2-22": dict(
 es="Daniel dice esto de noche, después de que se le revelara el sueño del rey. Ya se había ordenado ejecutar a todos los sabios de Babilonia, él incluido.",
 fr="Daniel dit cela la nuit, après que le songe du roi lui a été révélé. L’exécution de tous les sages de Babylone avait déjà été ordonnée, lui compris.",
 de="Daniel sagt das nachts, nachdem ihm der Traum des Königs offenbart wurde. Die Hinrichtung aller Weisen Babylons war bereits befohlen, ihn eingeschlossen."),
"hos-6-6": dict(
 es="Jesús cita esta línea dos veces en discusiones sobre con quién se puede comer y qué se puede hacer en sábado. En Oseas se dice del culto formal.",
 fr="Jésus cite cette ligne deux fois dans des discussions sur avec qui l’on peut manger et ce qu’on peut faire le sabbat. Chez Osée, elle vise le culte formel.",
 de="Jesus zitiert diese Zeile zweimal in Streitgesprächen darüber, mit wem man essen und was man am Sabbat tun darf. Bei Hosea gilt sie dem förmlichen Kult."),
"jol-2-28": dict(
 es="La profecía enumera a quienes normalmente no recibían palabra: hijos e hijas, viejos, jóvenes, siervos y siervas. La lista misma es la noticia.",
 fr="La prophétie énumère ceux qui d’ordinaire ne recevaient pas de parole : fils et filles, vieillards, jeunes gens, serviteurs et servantes. La liste est la nouvelle.",
 de="Die Weissagung zählt jene auf, die sonst kein Wort erhielten: Söhne und Töchter, Alte, Junge, Knechte und Mägde. Die Liste selbst ist die Nachricht."),
"jon-4-2": dict(
 es="Jonás explica por qué huyó: sabía desde el principio que la ciudad se salvaría. Es justamente la misericordia lo que le enfada, nada más.",
 fr="Jonas explique pourquoi il a fui : il savait dès le début que la ville serait épargnée. C’est précisément la miséricorde qui le met en colère, rien d’autre.",
 de="Jona erklärt, warum er floh: er wusste von Anfang an, dass die Stadt verschont würde. Genau die Barmherzigkeit ist es, worüber er zornig ist, sonst nichts."),
"mic-4-4": dict(
 es="La imagen de la paz no es un palacio, sino la propia vid y la propia higuera, sin nadie que atemorice. La medida de bienestar del profeta es doméstica.",
 fr="L’image de la paix n’est pas un palais mais sa propre vigne et son propre figuier, sans personne pour effrayer. La mesure du bien-être est ici domestique.",
 de="Das Friedensbild ist kein Palast, sondern der eigene Weinstock und Feigenbaum, ohne jemanden, der schreckt. Das Maß des Wohlergehens ist ganz häuslich."),
"hag-2-4": dict(
 es="Dicho a los constructores del segundo templo, a quienes los viejos dicen que el primero era incomparablemente mejor. La instrucción es simple: sed fuertes y trabajad.",
 fr="Dit aux bâtisseurs du second temple, à qui les anciens répètent que le premier était incomparablement plus beau. L’instruction est simple : soyez forts et travaillez.",
 de="Gesagt zu den Erbauern des zweiten Tempels, denen die Alten sagen, der erste sei unvergleichlich besser gewesen. Die Anweisung ist schlicht: seid stark und arbeitet."),
"zec-9-12": dict(
 es="La expresión «presos de esperanza» es una paradoja deliberada: el pueblo sigue cautivo, y la esperanza se nombra como lo que lo sostiene, no lo que lo liberó.",
 fr="L’expression « prisonniers de l’espérance » est un paradoxe voulu : le peuple est encore captif, et l’espérance est nommée comme ce qui le tient, non ce qui l’a libéré.",
 de="Der Ausdruck „Gefangene der Hoffnung“ ist ein bewusstes Paradox: das Volk ist noch gefangen, und die Hoffnung wird als das genannt, was es hält, nicht befreit."),
"mat-5-44": dict(
 es="Del Sermón del Monte. Los oyentes vivían bajo ocupación romana, así que «enemigo» significaba para ellos personas armadas concretas, no una abstracción.",
 fr="Du Sermon sur la montagne. Les auditeurs vivaient sous occupation romaine : « ennemi » désignait pour eux des gens armés précis, non une abstraction.",
 de="Aus der Bergpredigt. Die Zuhörer lebten unter römischer Besatzung, „Feind“ meinte für sie konkrete bewaffnete Menschen, keine Abstraktion."),
"mat-11-29": dict(
 es="Dicho en Galilea a quienes ya no pueden más. El yugo se ponía sobre una pareja: el animal joven aprendía andando junto a uno adulto, no solo.",
 fr="Dit en Galilée à ceux qui n’en peuvent plus. Le joug se posait sur une paire : le jeune animal apprenait en marchant près d’un adulte, non seul.",
 de="In Galiläa zu denen gesagt, die nicht mehr können. Das Joch legte man einem Paar auf: das junge Tier lernte neben einem erwachsenen, nicht allein."),
"mat-18-21": dict(
 es="Pedro propone perdonar siete veces creyéndolo generoso: los rabinos de entonces hablaban de tres. La respuesta lleva la cuenta a donde contar no tiene sentido.",
 fr="Pierre propose de pardonner sept fois, croyant être généreux : les rabbins de l’époque parlaient de trois. La réponse porte le compte là où compter n’a plus de sens.",
 de="Petrus schlägt sieben Mal Vergebung vor und hält das für großzügig: die Rabbinen sprachen von drei. Die Antwort verschiebt die Zahl dorthin, wo Zählen sinnlos wird."),
"mat-23-37": dict(
 es="Dicho sobre la ciudad al final de un discurso de reproche. La imagen de una gallina con sus polluelos rompe el tono de golpe, y acaba en «no quisisteis».",
 fr="Dit sur la ville à la fin d’un discours de reproche. L’image d’une poule et de ses poussins rompt le ton d’un coup, et cela finit par « vous n’avez pas voulu ».",
 de="Über die Stadt gesagt, am Ende einer Scheltrede. Das Bild der Henne mit Küken bricht den Ton abrupt, und es endet mit „ihr habt nicht gewollt“."),
"mat-26-41": dict(
 es="Dicho a discípulos que se durmieron en el huerto mientras él oraba. Lucas añade que dormían de tristeza, no por descuido.",
 fr="Dit à des disciples endormis au jardin pendant qu’il priait. Luc ajoute qu’ils dormaient de tristesse, non par négligence.",
 de="Gesagt zu Jüngern, die im Garten einschliefen, während er betete. Lukas fügt hinzu, dass sie aus Trauer schliefen, nicht aus Nachlässigkeit."),
"mrk-2-17": dict(
 es="Respuesta a escribas indignados de que comiera con recaudadores. El argumento es médico, y se pronunció a la mesa de uno de ellos.",
 fr="Réponse à des scribes indignés qu’il mange avec des collecteurs d’impôts. L’argument est médical, et il fut prononcé à la table de l’un d’eux.",
 de="Die Antwort an Schriftgelehrte, die sich empörten, dass er mit Zöllnern aß. Das Argument ist medizinisch — und es fiel am Tisch eines von ihnen."),
"mrk-9-23": dict(
 es="Respuesta al padre que dijo «si puedes». Jesús le devuelve el «si», y la siguiente frase del padre se vuelve la respuesta más honrada de los Evangelios.",
 fr="Réponse au père qui a dit « si tu peux ». Jésus lui rend ce « si », et la phrase suivante du père devient la réponse la plus honnête des Évangiles.",
 de="Die Antwort an den Vater, der sagte „wenn du kannst“. Jesus gibt ihm das „wenn“ zurück, und der nächste Satz des Vaters wird die ehrlichste Antwort der Evangelien."),
"mrk-14-8": dict(
 es="Dicho sobre una mujer que derramó perfume caro sobre su cabeza. Los presentes se indignaron por el derroche; él no midió la cantidad sino el momento.",
 fr="Dit d’une femme qui versa un parfum coûteux sur sa tête. Les présents s’indignèrent du gaspillage ; lui mesura non la quantité mais le moment.",
 de="Gesagt über eine Frau, die teures Salböl über seinen Kopf goss. Die Anwesenden empörten sich über die Verschwendung; er maß nicht die Menge, sondern den Zeitpunkt."),
"luk-2-19": dict(
 es="Dicho de María la noche en que llegaron los pastores con su relato de ángeles. Todos los demás se maravillaban en voz alta; ella calló y lo guardó.",
 fr="Dit de Marie la nuit où les bergers vinrent avec leur récit d’anges. Tous les autres s’étonnaient à voix haute ; elle ne dit rien et le garda.",
 de="Gesagt über Maria in der Nacht, als die Hirten mit ihrem Engelsbericht kamen. Alle anderen staunten laut; sie schwieg und bewahrte es."),
"luk-22-32": dict(
 es="Dicho a Pedro antes de la negación, no después. Jesús no promete que no caerá; dice que oró por su fe, y le da una tarea para después.",
 fr="Dit à Pierre avant le reniement, non après. Jésus ne promet pas qu’il ne tombera pas ; il dit avoir prié pour sa foi, et lui donne une tâche pour après.",
 de="Gesagt zu Petrus vor der Verleugnung, nicht danach. Jesus verspricht nicht, dass er nicht fällt; er sagt, er habe für seinen Glauben gebetet, und gibt ihm eine Aufgabe."),
"luk-22-61": dict(
 es="Pedro lo niega por tercera vez, canta un gallo, y Jesús, mientras lo llevan por el patio, se vuelve y lo mira. No se cruza ninguna palabra.",
 fr="Pierre le renie une troisième fois, un coq chante, et Jésus, qu’on mène à travers la cour, se retourne et le regarde. Aucun mot n’est échangé.",
 de="Petrus verleugnet ihn zum dritten Mal, ein Hahn kräht, und Jesus dreht sich, während man ihn über den Hof führt, um und sieht ihn an. Kein Wort fällt."),
"jhn-2-5": dict(
 es="Últimas palabras de María en los Evangelios, dichas a unos criados en una boda donde se acabó el vino. En el Evangelio de Juan ya no dice nada más.",
 fr="Derniers mots de Marie dans les Évangiles, dits à des serviteurs lors d’une noce où le vin a manqué. Dans l’Évangile de Jean, elle ne dit plus rien.",
 de="Marias letzte Worte in den Evangelien, gesagt zu Dienern bei einer Hochzeit, auf der der Wein ausging. Im Johannesevangelium sagt sie danach nichts mehr."),
"jhn-5-6": dict(
 es="La pregunta se hace a un hombre que llevaba treinta y ocho años junto al estanque. No responde que sí; explica por qué nunca le sale bien.",
 fr="La question est posée à un homme couché près de la piscine depuis trente-huit ans. Il ne répond pas oui ; il explique pourquoi cela ne marche jamais.",
 de="Die Frage gilt einem Mann, der achtunddreißig Jahre am Teich lag. Er antwortet nicht mit Ja; er erklärt, warum es nie klappt."),
"jhn-13-7": dict(
 es="Respuesta a Pedro, que se negaba a que le lavaran los pies. La promesa de comprender se coloca en el futuro, no se da en el acto.",
 fr="Réponse à Pierre, qui refusait qu’on lui lave les pieds. La promesse de comprendre est placée au futur, elle n’est pas donnée sur-le-champ.",
 de="Die Antwort an Petrus, der sich die Füße nicht waschen lassen wollte. Die Zusage des Verstehens wird in die Zukunft gelegt, nicht sofort gegeben."),
"jhn-14-18": dict(
 es="La palabra traducida «huérfanos» significa literalmente privados de un padre. Dicho a discípulos horas antes de que lo pierdan.",
 fr="Le mot rendu par « orphelins » signifie littéralement privés d’un parent. Dit à des disciples quelques heures avant qu’ils ne le perdent.",
 de="Das mit „Waisen“ übersetzte Wort heißt wörtlich eines Elternteils beraubt. Gesagt zu Jüngern, Stunden bevor sie ihn verlieren."),
"jhn-19-30": dict(
 es="Última palabra desde la cruz en el Evangelio de Juan, una sola palabra en griego. Se usaba en los recibos para marcar una deuda pagada por entero.",
 fr="Dernier mot depuis la croix dans l’Évangile de Jean, un seul mot en grec. On l’employait sur les reçus pour marquer une dette entièrement acquittée.",
 de="Das letzte Wort vom Kreuz im Johannesevangelium, im Griechischen ein einziges Wort. Man nutzte es auf Quittungen, um eine voll bezahlte Schuld zu vermerken."),
"jhn-20-15": dict(
 es="María llora junto al sepulcro vacío y lo toma por el hortelano. Lo reconoce no por la vista, sino cuando él dice su nombre.",
 fr="Marie pleure près du tombeau vide et le prend pour le jardinier. Elle le reconnaît non à la vue, mais quand il prononce son nom.",
 de="Maria weint am leeren Grab und hält ihn für den Gärtner. Sie erkennt ihn nicht am Aussehen, sondern als er ihren Namen sagt."),
"act-3-6": dict(
 es="Pedro responde a un mendigo a la puerta del templo que le había pedido dinero. Empieza admitiendo que no tiene, y solo entonces ofrece otra cosa.",
 fr="Pierre répond à un mendiant à la porte du temple qui lui demandait de l’argent. Il commence par avouer qu’il n’en a pas, et alors seulement offre autre chose.",
 de="Petrus antwortet einem Bettler am Tempeltor, der ihn um Geld gebeten hatte. Er beginnt mit dem Eingeständnis, keines zu haben, und bietet erst dann etwas anderes."),
"act-14-22": dict(
 es="Pablo dice esto tras volver a una ciudad donde poco antes lo habían apedreado y arrastrado fuera de las murallas, dándolo por muerto.",
 fr="Paul dit cela après être revenu dans une ville où, peu avant, on l’avait lapidé et traîné hors des murs en le croyant mort.",
 de="Paulus sagt das, nachdem er in eine Stadt zurückkehrte, in der man ihn kurz zuvor gesteinigt und für tot vor die Mauern geschleift hatte."),
"act-28-15": dict(
 es="Llevan a Pablo a Roma bajo custodia, y los cristianos romanos caminan muchas millas a su encuentro. Lucas anota que al verlos Pablo cobró ánimo.",
 fr="On mène Paul à Rome sous garde, et les chrétiens romains marchent de nombreux milles à sa rencontre. Luc note qu’en les voyant Paul reprit courage.",
 de="Paulus wird unter Bewachung nach Rom gebracht, und römische Christen gehen ihm viele Meilen entgegen. Lukas notiert, dass Paulus bei ihrem Anblick Mut fasste."),
"rom-5-3": dict(
 es="Una cadena de cuatro eslabones con la aflicción en primer lugar. Pablo no dice que la aflicción sea buena; describe qué crece de ella cuando se soporta.",
 fr="Une chaîne de quatre maillons, l’affliction en premier. Paul ne dit pas que l’affliction est bonne ; il décrit ce qui en pousse lorsqu’elle est endurée.",
 de="Eine Kette aus vier Gliedern, die Bedrängnis zuerst. Paulus sagt nicht, Bedrängnis sei gut; er beschreibt, was aus ihr wächst, wenn man sie aushält."),
"rom-12-1": dict(
 es="Frase deliberadamente contradictoria: un sacrificio es por definición algo muerto, y aquí se llama vivo. Así empieza la mitad práctica de la carta.",
 fr="Formule volontairement contradictoire : un sacrifice est par définition mort, et il est ici dit vivant. Ainsi commence la moitié pratique de la lettre.",
 de="Eine bewusst widersprüchliche Wendung: ein Opfer ist per Definition tot, und hier heißt es lebendig. So beginnt der praktische Teil des Briefes."),
"1co-3-6": dict(
 es="Pablo se dirige a una división en la comunidad donde unos se llamaban suyos y otros de Apolo. Divide el trabajo en etapas para quitar el motivo de discutir.",
 fr="Paul s’adresse à une division dans la communauté où les uns se disaient siens et les autres d’Apollos. Il découpe le travail en étapes pour ôter le motif de dispute.",
 de="Paulus wendet sich an eine Spaltung, in der die einen sich zu ihm, die anderen zu Apollos zählten. Er teilt die Arbeit in Etappen, um den Streitgrund zu nehmen."),
"1co-12-26": dict(
 es="De la comparación de la comunidad con un cuerpo. El argumento es fisiológico: un dolor en un sitio lo siente todo el organismo, y la buena voluntad no interviene.",
 fr="De la comparaison de la communauté à un corps. L’argument est physiologique : une douleur quelque part est ressentie par tout l’organisme, sans que la bonne volonté y soit.",
 de="Aus dem Vergleich der Gemeinde mit einem Leib. Das Argument ist physiologisch: Schmerz an einer Stelle spürt der ganze Körper, und guter Wille spielt keine Rolle."),
"1co-13-12": dict(
 es="Los espejos de entonces eran de bronce pulido y daban un reflejo borroso. La imagen habla de la calidad de la vista, no de la distancia.",
 fr="Les miroirs d’alors étaient de bronze poli et rendaient un reflet flou. L’image porte sur la qualité de la vue, non sur la distance.",
 de="Die Spiegel jener Zeit waren aus poliertem Bronze und gaben ein unscharfes Bild. Es geht um die Qualität des Sehens, nicht um Entfernung."),
"1co-15-10": dict(
 es="Pablo acaba de llamarse el menor de los apóstoles e indigno del nombre, por haber perseguido a la iglesia. La línea sobre la gracia responde a su propia acusación.",
 fr="Paul vient de se dire le moindre des apôtres et indigne de ce nom, pour avoir persécuté l’Église. La ligne sur la grâce répond à sa propre accusation.",
 de="Paulus hat sich eben den geringsten der Apostel und des Namens unwürdig genannt, weil er die Gemeinde verfolgte. Die Zeile über die Gnade beantwortet seinen eigenen Vorwurf."),
"2co-4-7": dict(
 es="Las vasijas de barro eran los recipientes más baratos, y no daba pena romperlos. El contraste entre contenido y envase es todo el sentido.",
 fr="Les vases d’argile étaient les récipients les moins chers, sans regret s’ils se cassaient. Le contraste entre contenu et contenant est tout le propos.",
 de="Tongefäße waren die billigsten Behälter, um die es nicht schade war, wenn sie zerbrachen. Der Gegensatz von Inhalt und Verpackung ist der ganze Punkt."),
"2co-5-7": dict(
 es="Línea breve dentro de un razonamiento de que lo visible es pasajero. El contraste no es entre fe y razón, sino entre fe y vista.",
 fr="Ligne brève à l’intérieur d’un raisonnement selon lequel le visible est passager. Le contraste n’est pas entre foi et raison, mais entre foi et vue.",
 de="Eine kurze Zeile innerhalb der Überlegung, dass das Sichtbare vergänglich ist. Der Gegensatz ist nicht Glaube und Vernunft, sondern Glaube und Sehen."),
"2co-7-6": dict(
 es="Pablo escribe que en Macedonia no tuvo descanso y fue atribulado por todos lados. El consuelo no llegó por una revelación, sino porque llegó una persona: Tito.",
 fr="Paul écrit qu’en Macédoine il n’eut aucun repos et fut pressé de toutes parts. La consolation ne vint pas par une révélation mais par l’arrivée d’une personne : Tite.",
 de="Paulus schreibt, er habe in Makedonien keine Ruhe gehabt und sei von allen Seiten bedrängt worden. Der Trost kam nicht durch eine Offenbarung, sondern durch Titus."),
"gal-6-7": dict(
 es="Imagen agrícola, del todo cotidiana: lo que se siembra es lo que crece, al margen de las intenciones. Dicho al final de una carta dura.",
 fr="Image agricole, tout à fait quotidienne : ce qu’on sème est ce qui pousse, quelles que soient les intentions. Dit à la fin d’une lettre sévère.",
 de="Ein bäuerliches, ganz alltägliches Bild: was gesät wird, wächst — unabhängig von den Absichten. Gesagt am Ende eines scharfen Briefes."),
"eph-2-10": dict(
 es="La palabra traducida «hechura» es la raíz griega de «poema». La línea viene justo después de la afirmación de que la salvación no es por obras.",
 fr="Le mot rendu par « ouvrage » est la racine grecque de « poème ». La ligne vient juste après l’affirmation que le salut n’est pas par les œuvres.",
 de="Das mit „Werk“ übersetzte Wort ist die griechische Wurzel von „Gedicht“. Die Zeile folgt direkt auf die Aussage, dass die Rettung nicht aus Werken kommt."),
"php-2-14": dict(
 es="La instrucción viene justo después del himno sobre Cristo que se despojó. La exigencia de no murmurar se plantea como conclusión sacada de ese himno.",
 fr="L’instruction vient juste après l’hymne sur le Christ qui s’est dépouillé. L’exigence de ne pas murmurer est posée comme la conclusion tirée de cet hymne.",
 de="Die Anweisung folgt unmittelbar auf den Hymnus über Christus, der sich entäußerte. Die Forderung, nicht zu murren, steht als Schlussfolgerung daraus."),
"col-3-12": dict(
 es="El verbo «vestíos» habla de ropas que se ponen adrede cada mañana. Justo antes, el hombre viejo se describe como algo que se quita como un manto.",
 fr="Le verbe « revêtez-vous » parle de vêtements qu’on met exprès chaque matin. Juste avant, le vieil homme est décrit comme ce qu’on ôte comme un manteau.",
 de="Das Verb „zieht an“ meint Kleider, die man jeden Morgen bewusst anlegt. Kurz davor wird der alte Mensch als etwas beschrieben, das man wie ein Gewand ablegt."),
"1th-5-14": dict(
 es="Tres grupos y tres enfoques distintos: amonestad a los ociosos, consolad a los pusilánimes, sostened a los débiles. Pablo distingue quién necesita qué.",
 fr="Trois groupes et trois approches différentes : avertissez les oisifs, consolez les découragés, soutenez les faibles. Paul distingue qui a besoin de quoi.",
 de="Drei Gruppen und drei verschiedene Zugänge: ermahnt die Müßigen, tröstet die Kleinmütigen, stützt die Schwachen. Paulus unterscheidet, wer was braucht."),
"2th-3-3": dict(
 es="Viene justo después de admitir que no todos tienen fe. La afirmación sobre la fidelidad de Dios se contrapone a la poca fiabilidad de las personas.",
 fr="Cela vient juste après l’aveu que tous n’ont pas la foi. L’affirmation sur la fidélité de Dieu s’oppose au peu de fiabilité des gens.",
 de="Es folgt direkt auf das Eingeständnis, dass nicht alle Glauben haben. Die Aussage über Gottes Treue steht gegen die Unzuverlässigkeit der Menschen."),
"1ti-1-15": dict(
 es="Pablo se llama el primero de los pecadores en presente, no en pasado. Después explica que justo por eso se le tuvo misericordia: como ejemplo.",
 fr="Paul se dit le premier des pécheurs au présent, non au passé. Il explique ensuite que c’est précisément pour cela qu’il a obtenu miséricorde : en exemple.",
 de="Paulus nennt sich den ersten der Sünder im Präsens, nicht in der Vergangenheit. Danach erklärt er, genau darum sei ihm Erbarmen widerfahren: als Beispiel."),
"2ti-2-13": dict(
 es="Última línea de un himno cristiano temprano que Pablo cita. De las cuatro líneas es la única que rompe la simetría: la respuesta no es un espejo.",
 fr="Dernière ligne d’une hymne chrétienne ancienne que Paul cite. Des quatre lignes, elle seule rompt la symétrie : la réponse n’est pas un miroir.",
 de="Die letzte Zeile eines frühchristlichen Hymnus, den Paulus zitiert. Von den vier Zeilen bricht nur sie die Symmetrie: die Antwort ist kein Spiegel."),
"2ti-4-17": dict(
 es="Pablo escribe que en su primera vista nadie compareció y todos lo abandonaron. Pide que no se les tenga en cuenta, y dice quién sí estuvo con él.",
 fr="Paul écrit qu’à sa première audience personne ne vint et que tous l’abandonnèrent. Il demande que cela ne leur soit pas imputé, et dit qui l’a soutenu.",
 de="Paulus schreibt, bei seiner ersten Verhandlung sei niemand gekommen und alle hätten ihn verlassen. Er bittet, es ihnen nicht anzurechnen, und sagt, wer beistand."),
"heb-2-18": dict(
 es="El argumento se apoya en la experiencia: ayuda quien ha pasado por ello. El verbo traducido «tentado» significa aquí ser probado al límite, no ser seducido.",
 fr="L’argument repose sur l’expérience : aide celui qui est passé par là. Le verbe rendu par « tenté » signifie ici être éprouvé jusqu’au bout, non séduit.",
 de="Das Argument stützt sich auf Erfahrung: es hilft, wer es durchgemacht hat. Das mit „versucht“ übersetzte Verb meint bis an die Grenze geprüft, nicht verlockt."),
"heb-13-2": dict(
 es="Alusión a Abraham recibiendo a tres viajeros junto a los encinos, y a Lot. El punto es que ninguno sabía a quién recibía; si no, el argumento falla.",
 fr="Allusion à Abraham recevant trois voyageurs près des chênes, et à Lot. Le point est qu’aucun ne savait qui il recevait ; sinon l’argument tombe.",
 de="Eine Anspielung auf Abraham, der drei Reisende bei den Eichen aufnahm, und auf Lot. Entscheidend ist, dass keiner wusste, wen er aufnahm; sonst trägt es nicht."),
"jas-2-17": dict(
 es="Justo antes va un ejemplo: a alguien sin ropa ni comida se le dice «id en paz, calentaos» y no se le da nada. La conclusión sale de ese ejemplo.",
 fr="Juste avant vient un exemple : à quelqu’un sans vêtement ni nourriture on dit « allez en paix, chauffez-vous » sans rien donner. La conclusion en découle.",
 de="Kurz davor steht ein Beispiel: einem ohne Kleidung und Essen sagt man „geht hin in Frieden, wärmt euch“ und gibt nichts. Daraus folgt der Schluss."),
"jas-4-6": dict(
 es="Cita de los Proverbios traída en medio de un análisis de las peleas en la comunidad. Santiago explica de dónde salen las riñas y halla la causa en los deseos.",
 fr="Citation des Proverbes placée au milieu d’une analyse des querelles dans la communauté. Jacques explique d’où viennent les disputes et en trouve la cause dans les désirs.",
 de="Ein Zitat aus den Sprüchen, mitten in einer Analyse der Streitigkeiten in der Gemeinde. Jakobus erklärt, woher der Zank kommt, und findet die Ursache in den Begierden."),
"jas-5-7": dict(
 es="La imagen de un labrador que espera la lluvia. Aquella tierra tenía dos estaciones de lluvia, temprana y tardía, y entre ellas no quedaba sino esperar.",
 fr="L’image d’un cultivateur qui attend la pluie. Cette terre avait deux saisons de pluie, la précoce et la tardive, et entre les deux il ne restait qu’à attendre.",
 de="Das Bild eines Bauern, der auf Regen wartet. Jenes Land hatte zwei Regenzeiten, Früh- und Spätregen, und dazwischen blieb nichts als Warten."),
"1pe-4-8": dict(
 es="La línea siguiente explica cómo se ve esto en la práctica: acogeos unos a otros sin murmurar. Era gente que vivía apretada y pobre.",
 fr="La ligne suivante explique à quoi cela ressemble en pratique : accueillez-vous les uns les autres sans murmurer. C’étaient des gens vivant serrés et pauvres.",
 de="Die nächste Zeile erklärt, wie das praktisch aussieht: nehmt einander auf ohne Murren. Es waren Menschen, die eng beieinander und arm lebten."),
"1pe-5-8": dict(
 es="Pedro escribe a los perseguidos y añade que lo mismo les ocurre a sus hermanos por todo el mundo. El consuelo aquí es que no están solos en ello.",
 fr="Pierre écrit aux persécutés et ajoute que la même chose arrive à leurs frères dans le monde entier. La consolation ici est qu’ils n’y sont pas seuls.",
 de="Petrus schreibt an Verfolgte und fügt hinzu, dass ihren Brüdern in der ganzen Welt dasselbe widerfährt. Der Trost hier ist, dass sie damit nicht allein sind."),
"1jn-3-20": dict(
 es="Se trata del caso en que el propio corazón acusa a la persona. Juan no discute con la acusación; dice que hay un tribunal más alto que el corazón.",
 fr="Il s’agit du cas où le cœur d’une personne l’accuse. Jean ne discute pas l’accusation ; il dit qu’il existe un tribunal plus haut que le cœur.",
 de="Es geht um den Fall, dass das eigene Herz einen Menschen anklagt. Johannes bestreitet die Anklage nicht; er sagt, es gebe ein höheres Gericht als das Herz."),
"jud-1-24": dict(
 es="Líneas finales de una carta breve, dedicada casi por entero a advertencias sobre el engaño. Termina no con una amenaza, sino con la promesa de sostener a alguien.",
 fr="Lignes finales d’une courte lettre, presque entièrement consacrée aux mises en garde contre la tromperie. Elle finit non par une menace mais par la promesse de soutenir.",
 de="Die Schlusszeilen eines kurzen Briefes, der fast ganz aus Warnungen vor Täuschung besteht. Er endet nicht mit einer Drohung, sondern mit der Zusage, jemanden zu halten."),
"rev-1-17": dict(
 es="Juan escribe que cayó como muerto ante la visión. Lo primero que oye no es una explicación, sino «no temas», con una mano puesta sobre él.",
 fr="Jean écrit qu’il tomba comme mort devant la vision. La première chose qu’il entend n’est pas une explication mais « ne crains pas », une main posée sur lui.",
 de="Johannes schreibt, er sei bei der Erscheinung wie tot hingefallen. Das Erste, was er hört, ist keine Erklärung, sondern „fürchte dich nicht“, mit einer Hand auf ihm."),
"rev-7-17": dict(
 es="Dicho sobre gente que salió de la gran tribulación. La imagen está invertida a propósito: al cordero se le llama pastor que lleva a fuentes de agua.",
 fr="Dit de gens sortis de la grande tribulation. L’image est inversée à dessein : l’agneau est appelé berger qui conduit aux sources d’eau.",
 de="Gesagt über Menschen, die aus der großen Bedrängnis kamen. Das Bild ist absichtlich umgekehrt: das Lamm heißt Hirte, der zu Wasserquellen führt."),
"rev-14-13": dict(
 es="Uno de los pocos lugares del libro donde una voz manda escribir algo aparte. Dicho de quienes murieron bajo persecución: primero el descanso, luego sus obras.",
 fr="L’un des rares endroits du livre où une voix ordonne d’écrire quelque chose à part. Dit de ceux morts sous la persécution : d’abord le repos, ensuite leurs œuvres.",
 de="Eine der wenigen Stellen des Buches, an der eine Stimme befiehlt, etwas gesondert aufzuschreiben. Gesagt über Verfolgte: zuerst die Ruhe, danach ihre Werke."),
"rev-22-5": dict(
 es="Penúltima imagen del libro. La noche se nombra como lo que ya no existirá, y con ella la necesidad de una lámpara, donde todo empezó.",
 fr="Avant-dernière image du livre. La nuit est nommée comme ce qui n’existera plus, et avec elle le besoin d’une lampe, là où tout a commencé.",
 de="Das vorletzte Bild des Buches. Die Nacht wird als das genannt, was es nicht mehr geben wird, und mit ihr der Bedarf an einer Lampe — womit alles begann."),

}
