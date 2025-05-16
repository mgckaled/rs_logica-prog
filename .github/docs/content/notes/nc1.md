# Conteúdo Bônus - Estrutura de Dados

> retornar ao [README.md](../../../../README.md)

## Súmário

- [Conteúdo Bônus - Estrutura de Dados](#conteúdo-bônus---estrutura-de-dados)
  - [Súmário](#súmário)
    - [Estrutura de Dados Heap](#estrutura-de-dados-heap)
      - [Construção de Min-Heap e Max-Heap em Python](#construção-de-min-heap-e-max-heap-em-python)
      - [Fila de Prioridade com Heap](#fila-de-prioridade-com-heap)
      - [Heapsort (Ordenação por Heap)](#heapsort-ordenação-por-heap)
      - [Aplicações Típicas de Heaps](#aplicações-típicas-de-heaps)
    - [Estrutura de Dados Hash](#estrutura-de-dados-hash)
      - [Função Hash e Índice](#função-hash-e-índice)
      - [Colisões de Hash](#colisões-de-hash)
      - [Desempenho](#desempenho)
      - [Uso de Hash em Python: dicionários (`dict`)](#uso-de-hash-em-python-dicionários-dict)

### Estrutura de Dados Heap

Um **heap** (min-heap ou max-heap) é uma **árvore binária completa** que satisfaz a *propriedade de heap*. Na forma de *min-heap*, cada nó pai tem valor menor ou igual ao dos filhos, de modo que o **menor elemento está sempre na raiz**. Em um *max-heap*, a propriedade é invertida: cada nó pai tem valor maior ou igual ao dos filhos, e **o maior elemento fica na raiz**. A árvore é completa, ou seja, todos os níveis são totalmente preenchidos, exceto possivelmente o último (mais profundo), que é preenchido da esquerda para a direita. Graças a essa estrutura, os elementos podem ser armazenados eficientemente num **array**: não há necessidade de ponteiros, pois para um nó no índice *i* (raiz em 0) seus filhos estão em *2i+1* e *2i+2*, e o pai em *(i−1)//2*.

Os heaps são amplamente usados para implementar *filas de prioridade*, pois permitem acessar rapidamente o elemento de maior (ou menor) prioridade. As operações principais são **inserção** (empurrar um elemento, *push*), **remoção do topo** (remover o menor ou maior, *pop*) e **heapify** (construir ou restaurar o heap). Tipicamente, insere-se o elemento no fim do array (preenchendo o último nível) e depois o comparamos iterativamente com seu pai, trocando-os se necessário (up-heap) até restaurar a propriedade do heap; no pop, substitui-se a raiz pelo último elemento e aplicamos down-heap para reordenar. Ambas as operações de inserção e remoção custam *O(log n)* em média (onde *n* é o número de nós). Por fim, o algoritmo *heapify* pode transformar um array arbitrário num heap em tempo linear: o *Build-Heap* aplica repetidamente *heapify-down* de baixo para cima para satisfazer o invariante do heap.

- **Inserção (`heappush`)**: adiciona elemento e **heapifica para cima**, tempo O(log n).
- **Remoção do topo (`heappop`)**: retira raiz (mínimo em min-heap), substitui pela última folha e **heapifica para baixo**, tempo O(log n).
- **Heapify**: converte um array em heap (tempo *O(n)* no caso do *Build-Heap*).

#### Construção de Min-Heap e Max-Heap em Python

Em Python pode-se usar o módulo embutido [`heapq`](https://docs.python.org/3/library/heapq.html), que por padrão implementa um **min-heap** (menor valor em `heap[0]`). Por exemplo:

```python
import heapq

# Exemplo: construir um min-heap a partir de uma lista
lista = [5, 1, 8, 3, 2]
heapq.heapify(lista)   # transforma 'lista' em um min-heap em O(n)
print(lista)           # a lista agora representa um heap
print(lista[0])        # o menor elemento (raiz) do heap
```

Como `heapq` não fornece nativamente um max-heap, uma abordagem comum é **inverter o sinal** dos valores (ou usar uma classe wrapper). Por exemplo, para simular um max-heap pode-se armazenar valores negados:

```python
import heapq

# Usando sinal negativo para simular max-heap
valores = [5, 1, 8, 3, 2]
max_heap = [-x for x in valores]
heapq.heapify(max_heap)    # agora max_heap[0] é o menor valor negado (i.e. maior valor original)
print(-max_heap[0])        # imprime o maior valor original do heap
```

Outra técnica é usar uma classe que inverte a comparação (por exemplo, redefinir `__lt__`), mas em geral armazenar tuplas ou valores negativos é suficiente.

Também é possível usar funções internas do `heapq` (disponíveis em Python 3.5+) para max-heap: por exemplo, `heapq._heapify_max(lista)` constrói um max-heap in-place (embora iniciadores e pop sejam `heapq._heappop_max`), mas isso é pouco usual.

#### Fila de Prioridade com Heap

Um heap implementa eficientemente uma **fila de prioridade**: o elemento com menor (ou maior) “peso” fica sempre disponível na raiz. No Python, tipicamente usamos tuplas onde o primeiro elemento é a prioridade. Por exemplo, para simular tarefas com prioridades num min-heap:

```python
import heapq

# Fila de prioridade: (prioridade, tarefa)
fila = []
heapq.heappush(fila, (2, "Tarefa B"))
heapq.heappush(fila, (1, "Tarefa A"))
heapq.heappush(fila, (3, "Tarefa C"))

# Processa tarefas por ordem de prioridade (menor valor = maior prioridade)
while fila:
    pri, tarefa = heapq.heappop(fila)
    print(f"Processando {tarefa} com prioridade {pri}")
```

Saída:

```plaintext
Processando Tarefa A com prioridade 1
Processando Tarefa B com prioridade 2
Processando Tarefa C com prioridade 3
```

Como citado, “binary heaps are a common way of implementing priority queues”. Em outras palavras, um heap nos permite inserir elementos com prioridades arbitrárias e sempre retirar o de maior prioridade em tempo *O(log n)*. Em aplicações, piles de prioridade são usadas em **escalonamento de tarefas**, gerenciadores de sistemas operacionais e em algoritmos de grafos (por exemplo, Dijkstra). No caso de Dijkstra, por exemplo, atualiza-se as distâncias reduzidas inserindo cópias na fila de prioridade; retira-se repetidamente o vértice de menor distância para relaxar arestas.

#### Heapsort (Ordenação por Heap)

O *heapsort* é um algoritmo de ordenação que aproveita a estrutura heap. A ideia típica para ordenação crescente é:

1. Construir um **max-heap** a partir do array de entrada (para garantir que o maior elemento fique na raiz).
2. Repetidamente remover o elemento da raiz do heap (o maior) e colocá-lo no final do array ordenado.

Isso produz o array ordenado em ordem crescente. Como o heap pode ser implementado in-place num vetor (sem estruturas auxiliares), o heapsort também é um algoritmo in-place. Ele tem custo *O(n log n)* no pior caso. Em Python, podemos ilustrar de forma simples usando o `heapq` (min-heap) e invertendo valores, ou construindo o heap e extraindo todos os elementos. Por exemplo:

```python
import heapq

arr = [5, 3, 1, 4, 2]
heapq.heapify(arr)               # transforma em min-heap
ordenado = [heapq.heappop(arr)   # remove menores em sequência
            for _ in range(len(arr))]
print(ordenado)  # [1, 2, 3, 4, 5]
```

Neste exemplo usamos o min-heap para obter ordenação crescente (sempre removendo o menor). Em alternativa, para demonstrar a ideia clássica do max-heap, poderíamos usar `heapq._heapify_max` e `heapq._heappop_max` (funções internas) ou manipular sinais. O importante é que, a cada remoção, restauramos a propriedade do heap, resultando em *O(n log n)* de custo total. De fato, “binary heaps are also commonly employed in the heapsort sorting algorithm, which is an in-place algorithm”.

#### Aplicações Típicas de Heaps

Além de ordenação e filas de prioridade, heaps aparecem em várias áreas de ciência da computação. Exemplos comuns incluem:

- Escalonamento de tarefas**: sistemas operacionais usam heaps para escolher a próxima tarefa de maior prioridade.
- **Algoritmos de grafos**: Dijkstra e A\* usam heaps para selecionar o vértice de menor distância estimada em cada passo.
- **Gerenciamento de eventos**: simuladores de eventos discretos mantêm eventos futuros ordenados por timestamp.
- **Seleção de k-ésimos elementos**: encontrar os *k* menores ou maiores elementos de uma coleção, mantendo um heap de tamanho *k*.
- **Fila de prioridade abstrata**: em estruturas de dados e algoritmos em geral, sempre que for necessário acessar repetidamente o elemento de maior ou menor valor de um conjunto mutável, um heap é a solução padrão.

Em resumo, o heap é uma estrutura simples e poderosa: uma árvore binária completa armazenada em array, que garante acesso rápido ao elemento de extremidade (mínimo ou máximo) e suporta inserções e remoções em tempo logarítmico. Essa combinação de eficiência e simplicidade explica sua presença em muitos algoritmos e sistemas computacionais.

**Referências:** definições e propriedades de heap, representação interna em array, operações básicas e complexidades, uso em filas de prioridade e heapsort.

### Estrutura de Dados Hash

Hash (ou *tabela de dispersão*) é uma estrutura que armazena pares **chave-valor** de modo a permitir buscas muito rápidas. Em vez de procurar o dado sequencialmente, uma **função hash** transforma a chave (por exemplo, um nome) num índice numérico que aponta diretamente para o local onde o valor está armazenado. Por exemplo, imagine uma lista telefônica: em vez de folhear por cada nome, aplicamos um cálculo (hash) à palavra “Maria” para encontrar imediatamente o compartimento (bucket) certo e achar seu telefone. A Figura abaixo ilustra esse processo: cada nome (chave) é passado por uma função hash que gera um índice de bucket onde o número de telefone (valor) é guardado.

*Figura:* Diagrama simplificado de uma tabela hash (keys: nomes, buckets: telefones). A função hash converte cada nome em um índice, agilizando o acesso aos valores.

Internamente, uma tabela hash normalmente usa um **array** de tamanho fixo (ou que pode crescer), onde cada posição é chamada de *bucket* ou *slot*. A função hash recebe a chave e calcula um número inteiro; frequentemente calcula-se algo como `índice = hash(chave) % tamanho_array`. Isso garante que o índice esteja dentro dos limites do array. Como resultado, inserir ou buscar um valor requer apenas calcular a função hash e acessar o array naquele índice – em média, uma operação de tempo **constante** (O(1)), independente da quantidade de itens armazenados. Em Python, por exemplo, os [dicionários (`dict`)](https://docs.python.org/3/library/stdtypes.html#dict) usam tabelas hash internamente, o que dá complexidade O(1) para busca de chaves.

#### Função Hash e Índice

A **função hash** é o truque matemático que mapeia a chave para um número. Ela deve ser rápida e distribuir bem as chaves. Um método comum é somar ou multiplicar valores associados às partes da chave e depois usar o resto da divisão pelo tamanho do array. Por exemplo, para a string "abc", podemos definir `h = (ord('a')+ord('b')+ord('c'))`, e então `índice = h % tamanho`. O importante é que, idealmente, chaves diferentes gerem índices diferentes e bem espalhados, evitando sobrecarga num único bucket.

#### Colisões de Hash

Uma **colisão** ocorre quando duas chaves diferentes produzem o mesmo índice hash. Como há infinitas chaves possíveis e um número finito de buckets, colisões são inevitáveis em tabelas hash. No exemplo da tabela de telefones, seria como duas pessoas diferentes (“João” e “Maria”) acabarem mapeadas para o mesmo número de índice. Nesses casos, é preciso um **tratamento de colisão** para armazenar ambos os valores.

- **Encadeamento (separate chaining):** cada bucket guarda uma lista encadeada (ou outra estrutura) de pares chave-valor. Se há colisão, o novo par é adicionado à lista daquele bucket. Vantagem: simples de implementar. Desvantagem: se muita gente colidir num bucket, essa lista cresce e torna as buscas mais lentas (pode ficar O(n) no pior caso).
- **Endereçamento aberto (open addressing):** todos os pares ficam no próprio array. Se o bucket calculado já está ocupado, o algoritmo procura outro slot livre (por exemplo, pegando o próximo índice disponível ou usando uma técnica de *probing* como linear/quadrático). Assim, mesmo colidindo, o par acaba em outro índice. Isso evita listas ligadas, mas requer que o array tenha espaço livre extra (às vezes exigindo redimensionamento).

*Figura:* Exemplo de colisão em uma tabela hash. Várias chaves diferentes caíram no mesmo índice (por causa de uma função hash ruim), formando uma lista de valores no bucket índice 2. Esse cenário força a aplicar uma lista encadeada ou outra forma de tratamento de colisão.

*Figura:* Com uma função hash melhor, as mesmas chaves são espalhadas por índices diferentes (11, 14, 23, 38 neste exemplo). Assim reduzimos colisões e mantemos acesso rápido. Uma boa função hash tenta evitar que vários elementos acabem no mesmo índice.

#### Desempenho

Tabelas hash bem implementadas oferecem operações de inserção, busca e remoção muito rápidas, em tempo médio O(1). Ou seja, mesmo dobrando a quantidade de itens, o tempo de acesso continua essencialmente o mesmo. Esse desempenho constante é **amortizado**, porque ocasionalmente a tabela precisa ser redimensionada (por exemplo, dobrando de tamanho quando estiver muito cheia) para manter baixa a taxa de ocupação. Em geral, recomenda-se manter a **taxa de carga** (número de itens dividido pelo tamanho do array) razoavelmente baixa (por exemplo, abaixo de 70%) para evitar muitas colisões. Quando feito corretamente, o uso de tabelas hash é até mais eficiente que buscas em árvores, tornando-as muito comuns em caches, índices de bancos de dados e estruturas de dados associativas. Veja uma boa introdução em [GeeksforGeeks – Hashing Data Structure](https://www.geeksforgeeks.org/hashing-data-structure/) e uma visualização didática em [VisuAlgo – Hash Table](https://visualgo.net/en/hashtable).

#### Uso de Hash em Python: dicionários (`dict`)

Em Python, os [dicionários (`dict`)](https://docs.python.org/3/library/stdtypes.html#dict) são implementados sobre tabelas hash. Isso significa que, ao armazenar um par `chave: valor`, a linguagem usa o hash da chave para decidir onde guardar esse valor. Como resultado, acessos e inserções em um dict são extremamente rápidos na média. As **chaves** dos dicionários Python devem ser de tipos **imutáveis** (como strings, números, tuplas), pois cada chave precisa ter um valor de hash consistente. Além disso, cada chave é única: não pode haver duplicatas. Se você atribuir um valor a uma chave que já existe, o valor antigo será **sobrescrito** pelo novo.

```python
# Criando e acessando dados em um dicionário
cadastro = {"nome": "Ana", "idade": 30}  # cria um dicionário com duas chaves
print(cadastro["idade"])   # acessa o valor da chave "idade" (imprime 30)

cadastro["cidade"] = "Lisboa"  # adiciona um novo par chave-valor
print(cadastro)  # {'nome': 'Ana', 'idade': 30, 'cidade': 'Lisboa'}

cadastro["idade"] = 31   # sobrescreve o valor antigo da chave "idade"
print(cadastro)  # {'nome': 'Ana', 'idade': 31, 'cidade': 'Lisboa'}

print("idade" in cadastro)  # verifica existência (True)
del cadastro["idade"]        # remove o par chave-valor com chave "idade"
print(cadastro)  # {'nome': 'Ana', 'cidade': 'Lisboa'}
```

Alguns pontos importantes sobre `dict` em Python:

- **Chaves imutáveis:** apenas tipos como strings, números ou tuplas podem ser chaves. Por exemplo, `cadastro[("Rua A", 123)] = "Endereço"` funciona (tupla), mas `cadastro[["Rua A", 123]] = "Endereço"` dá erro de *unhashable type* (lista não pode ser chave).
- **Chaves únicas:** cada chave só aparece uma vez; redefinir a mesma chave atualiza o valor anterior. No exemplo acima, atribuir `cadastro["idade"]` duas vezes fez o dicionário manter apenas a última.
- **Acesso rápido:** como os dicionários usam hash, operações como `valor = cadastro[chave]` ou `if chave in cadastro` ocorrem em tempo constante médio (O(1)). Mesmo com muitos itens, o acesso permanece eficiente.
- **Métodos úteis:**

  - `cadastro.get(chave, valor_padrão)` retorna o valor associado ou `valor_padrão` caso a chave não exista (evita `KeyError`).
  - `cadastro.keys()`, `cadastro.values()`, `cadastro.items()` permitem iterar sobre chaves, valores ou pares.
  - `cadastro.pop(chave)` remove e retorna o valor.
  - Há ainda métodos como `.clear()` (limpar todos itens) ou `.update()` (atualizar com outro dicionário).

Abaixo, um exemplo prático: contar a frequência de palavras num texto. Cada palavra vira uma chave, e o valor é seu contador.

```python
texto = "gato cachorro gato passarinho cachorro"
contagem = {}
for palavra in texto.split():
    contagem[palavra] = contagem.get(palavra, 0) + 1

print(contagem)  # {'gato': 2, 'cachorro': 2, 'passarinho': 1}
```

Neste código, o dicionário `contagem` é usado para agrupar e contar palavras eficientemente. A cada palavra, acessamos (ou criamos) um item no dicionário e incrementamos seu contador. Graças ao hash interno, essas operações de leitura e atualização ocorrem muito rapidamente, mesmo que o texto seja grande.

**Resumo dos benefícios do hash/dict em Python:** ele permite organizar dados relacionados de forma clara (chave→valor), com acesso extremamente rápido, chaves únicas e flexibilidade de estrutura. Por exemplo, é comum usar dicionários para fazer cache de resultados ou contagem de itens, aproveitando sua alta eficiência em armazenamento e busca de dados agrupados em chaves.

Para leitura complementar:

- [Real Python – Dictionaries in Python](https://realpython.com/python-dicts/)
- [Wikipedia – Hash table](https://en.wikipedia.org/wiki/Hash_table)
- [MIT OCW – Hashing (Lecture Notes)](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/pages/lecture-notes/)
