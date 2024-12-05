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
