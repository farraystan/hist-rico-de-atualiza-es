from gtts import gTTS

# Texto que você quer converter
texto = "olá, o video é sobre organização, com tanta informação se movendo pelo mundo é possível acreditar de que não há informação completa no mundo e de que nunca encontraremos, porém a informação ela pode sim ter um fim, mas a maneira como a transmitimos é infinita o que faz a informação se multiplicar, entendendo isso, podemos ver que tanto a informação e a maneira de transmiti-la podem ser referidas apenas como informação, mas não é a palavra certa para isso, devemos encontrar a palavra que (se refere a maneira de transmitir informação) para distinguir de informação, existem muitas palavras que tenham a mesma referencia, mas nesse video vou usar a palavra apresentação, toda apresentação vem de um processamento da informação, quando recebemos informação através de uma apresentação, ou seja, por uma pessoa, não estaremos recebendo informação, e sim, uma inspiração para futuros processamentos da informação, pois a fonte da informação vem da criação original, dela aprendemos tudo o que sabemos, um computador só terá valor se houver energia entrando nele, a mesma coisa da mente, ela só terá valor se houver informação entrando nele, e se existe energia é por que existe uma fonte de energia, e essa fonte não veio do nada, sempre é alguem que faz algo, algo pode fazer algo, porém esse algo precisou ser feito por alguém para funcionar, e em tudo o que é feito primeiro houve expressão na mente(referencia biblia), ou seja, antes de contruir uma casa, primeiro teve que haver o projeto completo sobre a construção da casa antes de começar a contruir, sendo um projeto ou construção deve haver espaço para realizá-los, então o projeto foi feito dentro da mente que envia as instruções para realizar a contrução no espaço planejado, portanto existe um espaço interno onde é feito o planejamento, e o espaço exterior onde será feito a construção, no caso da criação do mundo, o espaço sempre existiu, mas estava vazio, a regra é que todas as coisas devem estar no espaço para existir, então deve haver uma mente imaterial que contenha todas as coisas que existem e que deveriam existir, como se todo o espaço e tudo o que ocorrese nele fosse obra de uma mente maior, ou seja, somos uma mente criada dentro da própria mente do criador, pois o único modo de aparecer qualquer coisa no espaço é através do poder da mente, mas não da mente humana, pois se imaginarmos água ela não irá aparecer externamente, só será uma imagem, a mente do criador não é por imaginação, é por referenciação, ou seja, indicando o que deveria aparecer primeiro de forma síncrona, significa que mesmo a informação não sendo vísivel na mente do criador o espaço ele pede para que essas coisas venha existir, então deve haver uma ordem, todo o pedido vem de uma necessidade, mas o espaço deve pedir na ordem certa, ele pode ter vários pedidos, mas o programa só executará um pedido de cada vez, e tudo apareceu de modo organizado no tempo e no espaço. o universo pode ser grande, mas a sua composição é o seu conhecimento, espero que todas as mentes que assistiram a esse video venham se abrir para entender uns aos outros, obrigado."

# Cria um objeto gTTS
tts = gTTS(text=texto, lang='pt-br')

# Salva o arquivo de áudio
tts.save("organização.mp3")
