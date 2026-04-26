from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.pre_tokenizers import Punctuation, Whitespace, Sequence
from tokenizers.trainers import BpeTrainer
import matplotlib.pyplot as plt

'''
tokenizer = Tokenizer(BPE()) #Aqui estamos a selecionar o algoritmo de aprendizagem de tokens (Existem outras opções)
tokenizer.pre_tokenizer = Sequence([Whitespace(), Punctuation()]) #Aqui selecionamos a forma como o texto vai ser pré processado antes do Tokenizer (Existem outras opções) (Pre-Tokenizer)
#Conclusão --> O BPE vai dividir o texto, o PRE_TOKENIZER diz como dividir
trainer = BpeTrainer( #Aqui definimos alguns parâmetros do treino
    vocab_size = 2500, #
    special_tokens = ["<bos>", "<eos>", "<pad>", "<newline>"] #Special_tokens são usados para indicar ao modelo inicio de uma sequencia, fim de uma sequencia, padding
)

tokenizer.train(files = ["Os Lusiadas.txt"], trainer = trainer) #Treino final com o dataset que vai ser usado para o modelo


with open ("Os Lusiadas.txt", "r", encoding = "utf-8") as file:
    texto = file.read()

print (len(texto))
print (texto[:1000])
'''



#Maneira mais fácil de entender como funciona um Tokenizer
#Primeiro - Pre-Tokenizer e depois aplicar o Treino

'''
with open ("Os Lusiadas.txt", "r", encoding = "utf-8") as file:
    texto = file.read()

pre_tokenizer = Sequence([Whitespace(), Punctuation(),]).pre_tokenize_str(texto)

tokenizer = Tokenizer(BPE())
trainer = BpeTrainer(
    vocab_size = 1000,
    special_tokens = ["<bos>", "<eos>", "<pad>", "<newline>"]
)

tokenizer.train(files = ["Pre-Tokenizer.txt"], trainer = trainer)


tokenization = tokenizer.encode(texto)

print (len(tokenization.tokens))
'''
vocabsize = [10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000]
numtoken = [210876, 211458, 212460, 213181, 214231, 214912, 215623, 217575, 220540, 228023]


plt.figure(figsize = (6, 7))
plt.plot(vocabsize, numtoken, marker = ".")

plt.xlabel("Tamanho do Vocabulário", size = 12)
plt.xticks(list(range(0, 11000, 1000)))
plt.ylabel("Número de Tokens", size = 12)
plt.yticks(list(range(200000, 250000, 2500)))

plt.show()



