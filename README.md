# NI-Dusaliev
[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Нейронные+сети+Дусалиев)](https://git.io/typing-svg)

Файлы заданий для запуска с тестами находятся в директории PE/nntask[n], где n - номер задания
## Задание 1
### Тесты:
*nntask1_input (1).txt*
```
(v1, v2 ,  2)
( v3   ,  v2, 1) (   v2, v3,   1)
    (v3, v1, 1)
```
*nntask1_input (2).txt*
```
(m1, m3, 2),
(g1, m1, 1),
(g2, g1, 3),
(m1, m2, 4)
```
*nntask1_input (3).txt*
```
(v1,v2,1),
(v2,v3,1),
(v1,v3,2),
(v3,v4,1),
(v1,v4,2),
(v4,v5,1),
(v4,v6,1),
(v5,v6,2),
(v2,v5,2)
```

### Запуск программы:
```
nntask1.exe input="nntask1_input (1).txt" output="nntask1_output (1).xml" ---> Успешный
nntask1.exe input="nntask1_input (2).txt" output="nntask1_output (2).xml" ---> Ошибочный
nntask1.exe input="nntask1_input (3).txt" output="nntask1_output (3).xml" ---> Успешный
```

## Задание 2
### Тесты:
*nntask1_output (1).xml*
```
<?xml version="1.0" encoding="utf-8"?>
<graph>
    <vertex>v1</vertex>
    <vertex>v2</vertex>
    <vertex>v3</vertex>
    <arc>
        <from>v1</from>
        <to>v2</to>
        <order>2</order>
    </arc>
    <arc>
        <from>v3</from>
        <to>v2</to>
        <order>1</order>
    </arc>
    <arc>
        <from>v2</from>
        <to>v3</to>
        <order>1</order>
    </arc>
    <arc>
        <from>v3</from>
        <to>v1</to>
        <order>1</order>
    </arc>
</graph>
```
*nntask1_output (3).xml*
```
<?xml version="1.0" encoding="utf-8"?>
<graph>
    <vertex>v1</vertex>
    <vertex>v2</vertex>
    <vertex>v3</vertex>
    <vertex>v4</vertex>
    <vertex>v5</vertex>
    <vertex>v6</vertex>
    <arc>
        <from>v1</from>
        <to>v2</to>
        <order>1</order>
    </arc>
    <arc>
        <from>v2</from>
        <to>v3</to>
        <order>1</order>
    </arc>
    <arc>
        <from>v1</from>
        <to>v3</to>
        <order>2</order>
    </arc>
    <arc>
        <from>v3</from>
        <to>v4</to>
        <order>1</order>
    </arc>
    <arc>
        <from>v1</from>
        <to>v4</to>
        <order>2</order>
    </arc>
    <arc>
        <from>v4</from>
        <to>v5</to>
        <order>1</order>
    </arc>
    <arc>
        <from>v4</from>
        <to>v6</to>
        <order>1</order>
    </arc>
    <arc>
        <from>v5</from>
        <to>v6</to>
        <order>2</order>
    </arc>
    <arc>
        <from>v2</from>
        <to>v5</to>
        <order>2</order>
    </arc>
</graph>
```

### Запуск программы:
```
nntask2.exe input="nntask1_output (1).xml" output="nntask2_output (1).txt" ---> Ошибочный
nntask2.exe input="nntask1_output (3).xml" output="nntask2_output (3).txt" ---> Успешный
```

## Задание 3
### Тесты:
*nntask1_output (3).xml*
```
<?xml version="1.0" encoding="utf-8"?>
<graph>
    <vertex>v1</vertex>
    <vertex>v2</vertex>
    <vertex>v3</vertex>
    <vertex>v4</vertex>
    <vertex>v5</vertex>
    <vertex>v6</vertex>
    <arc>
        <from>v1</from>
        <to>v2</to>
        <order>1</order>
    </arc>
    <arc>
        <from>v2</from>
        <to>v3</to>
        <order>1</order>
    </arc>
    <arc>
        <from>v1</from>
        <to>v3</to>
        <order>2</order>
    </arc>
    <arc>
        <from>v3</from>
        <to>v4</to>
        <order>1</order>
    </arc>
    <arc>
        <from>v1</from>
        <to>v4</to>
        <order>2</order>
    </arc>
    <arc>
        <from>v4</from>
        <to>v5</to>
        <order>1</order>
    </arc>
    <arc>
        <from>v4</from>
        <to>v6</to>
        <order>1</order>
    </arc>
    <arc>
        <from>v5</from>
        <to>v6</to>
        <order>2</order>
    </arc>
    <arc>
        <from>v2</from>
        <to>v5</to>
        <order>2</order>
    </arc>
</graph>
```
*nntask3_input2 (3).txt*
```
v1:*
v2:+
v3:+
v4:exp
v5:*
v6:*
```

### Запуск программы:
```
nntask3.exe input1="nntask1_output (3).xml" input2="nntask3_input2 (3).txt" output="nntask3_output (3).txt" ---> Успешный
```

## Задание 4
### Тесты:
*nntask4_input_1.txt*
```
[[0.2, 0.3, 0.9, 0.4], [0.7, 0.3, 0.1, 0.5], [0.6, 0.1, 0.2, 0.9], [0.3, 0.3, 0.3, 0.3], [0.0, 0.5, 1.0, 0.6]]
[[0.6, 0.7, 0.8, 0.9, 1.0], [0.301, 0.302, 0.303, 0.304, 0.305], [0.1, 0.2, 0.3, 0.2, 0.1]]
```
*nntask4_input_2.txt*
```
[5.81, 3.71, 6.21, 9.2]
```

### Запуск программы:
```
nntask4.exe input1=nntask4_input_1.txt input2=nntask4_input_2.txt output=nntask4_output.json ---> Успешный
```

## Задание 5
### Тесты:
*nntask5_input_1.json*
```
{
  "W1": [[0.6961299612330134, 0.28242546061882245, 0.05955962907940082, 0.024528745740088786,0.27562714731075544, 0.23696855935858063, 0.973907660957942, 0.37884189370425836, 0.01681891625824672, 0.7178806844970341, 0.23861644072411903, 0.20275934213843283, 0.3099976399971759, 0.5413836946844571, 0.456078021314988, 0.32145234525002, 0.215252039222, 0.921488201992382221, 0.57289199923882, 0.1237477217829, 0.39205217249399311, 0.12858829910023, 0.75882819923332, 0.1233322155212, 0.568882300258281, 0.2992993451200528, 0.127577291050291, 0.19924885735771289],
         [0.2850771910682419, 0.4333996587416823, 0.25909715973402525, 0.8079092422547227, 0.29427557712855534, 0.7946087712112367, 0.26854195934198355, 0.20509835578210733, 0.2476420800158753, 0.7729363510108873, 0.3009752495338631, 0.5758641218916277, 0.8444047030641744, 0.5784583077468011, 0.9389427951843039, 0.657289912883299123, 0.2149586829923881, 0.6920501274738845, 0.39159959602182485, 0.492395000581238, 0.62995120503582572, 0.1284828584757678, 0.9053828915285835, 0.1881583588518848, 0.129581285929591258, 0.912588383848818, 0.4912853859291581, 0.32815828582581],
         [0.45494523275777454, 0.8245742711666517, 0.07947102605976109, 0.47351435545455156, 0.9464118677499764, 0.3783517015138136, 0.5411487150194798, 0.16795126188047682, 0.08965624452410936, 0.019097347634274398, 0.8817200502974795, 0.63095342652293, 0.08336545804901863, 0.9672264484025755, 0.8928508852809949, 0.5832712854125895, 0.88272581258394972, 0.2188249323958341, 0.01259812584884842, 0.293948357732781, 0.91248357125923595, 0.8188824881420515, 0.01295388835818581, 0.9391925838599124, 0.12942958128593059, 0.5818250359203581, 0.401592358238503224, 0.293481582352301],
         [0.25888181451497705, 0.3625439206499408, 0.3108772833737167, 0.5578286378518442, 0.49982985857331885, 0.9679211228758094, 0.4432601254760452, 0.9517041804921835, 0.24850482468472512, 0.4541952511225863, 0.8944889377893879, 0.9961982281757301, 0.418934861672298, 0.9970261250995428, 0.6194547888205366, 0.915885923588194811, 0.1258736829349112, 0.19582385282691021, 0.2582739185293582, 0.4838258201493586, 0.18251264835620386, 0.9237467357239842, 0.9182429387523875, 0.2384625746838529, 0.28471264836239729, 0.352835723689855, 0.14823857235799128, 0.1925429387567369],
         [0.3998125815584943, 0.9426683521859932, 0.24515617730987416, 0.7691866708429562, 0.3136788757058868, 0.6113328319902603, 0.3402904721625274, 0.7564250536159476, 0.030894699092625766, 0.06560531390816293, 0.6554608677050607, 0.8323393790203365, 0.399712865980254, 0.684653315101575, 0.8157005138402356, 0.1249581825912931924, 0.12317571283912054, 0.192488357361124, 0.88284725120321485, 0.9128572317481319, 0.81284735992358128, 0.815883592306038, 0.38185810580238571, 0.3418582385283591, 0.91284715835203596, 0.931747127481580, 0.12477593820598203, 0.8812747195823855]
        ],
  "W2": [
         [0.2319608683474016, 0.5339203150969338, 0.5413589720635835, 0.4092732861530637, 0.23289492386916144],
         [0.4793214201058875, 0.6419292498517909, 0.7318669180700694, 0.15975375064907715, 0.4035801505652603],
         [0.5257211041600813, 0.5470324738739286, 0.930187501167203, 0.6987153855385628, 0.8491307804746495]
        ],
  "W3": [
         [0.5074978343217069, 0.8381272863105146, 0.6728481149249034]
        ]
}
```
*nntask5_input_2.json*
```
{
  "X": [
    [0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0],
    [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0],
    [0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0],
    [0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0],
    [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0],
    [0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0],
    [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
    [0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0],
    [0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0]
  ],
  "Y": [[0.0], [0.1], [0.2], [0.3], [0.4], [0.5], [0.6], [0.7], [0.8], [0.9]]
}
```
*nntask5_input_3.json*
```
{
  "iters": 25000,
  "alpha": 0.75,
  "eps": 0.000001
}
```

### Запуск программы:
```
nntask5.exe input1=nntask5_input_1.json input2=nntask5_input_2.json input3=nntask5_input_3.json output=nntask5_output.txt ---> Успешный
```
  [![HitCount](https://hits.dwyl.com/Takhirchik/NI-Dusaliev.svg?style=flat-square&show=unique)](http://hits.dwyl.com/Takhirchik/NI-Dusaliev)
