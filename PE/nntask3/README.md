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
