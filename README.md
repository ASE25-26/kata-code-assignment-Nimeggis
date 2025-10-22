# Übungsaufgabe: String Calculator Kata (Python)

Diese Übung gehört zu den Themen **Dojos, Katas, Clean Code und Software Craftsmanship**.  
Das Ziel ist es, in kleinen Schritten Test-Driven Development (TDD) zu üben und dabei **sauberen, gut lesbaren Code** zu schreiben.

---

## Ziel der Übung

Du sollst eine Funktion `add(numbers: str) -> int` (in src/string_calculator.py) implementieren, die Zahlen aus einem Textstring extrahiert und deren Summe berechnet. Dabei lernst du, wie man schrittweise vorgeht, um funktionalen und wartbaren Code zu erstellen.

---

## Vorgehen

Arbeite in kurzen Zyklen nach dem Prinzip:

1. **Test schreiben:** Formuliere zuerst einen Testfall, der das gewünschte Verhalten prüft.  
2. **Minimal implementieren:** Schreibe gerade so viel Code, dass der Test besteht.  
3. **Refaktorieren:** Verbessere deinen Code, ohne das Verhalten zu ändern (z. B. durch Umstrukturieren oder Vereinfachen).

---

## Prerequisite 

Für diese Übung solltest du sicherstellen, dass Python auf deinem System installiert ist.  
Zusätzlich benötigst du einige Pakete, um Tests durchzuführen und den Code zu überprüfen.

### Voraussetzungen:

- **Python:** Version 3.6 oder höher sollte installiert sein. Du kannst die Installation von Python von der offiziellen Webseite [python.org](https://www.python.org/downloads/) vornehmen.
- **Paket-Manager:** `pip` sollte verfügbar sein, um zusätzliche Pakete zu installieren.

### Benötigte Pakete:

- `flake8` für die Überprüfung des Codes auf Stil- und Syntaxfehler  
- `pylint` für eine statische Codeanalyse und Verbesserungsvorschläge

### Installation der Pakete:

Führe folgenden Befehl in deinem Terminal oder der Eingabeaufforderung aus, um alle benötigten Pakete zu installieren:

```bash
pip install flake8 pylint
```

---

## Regeln der Kata

Die Funktion `add` soll folgende Anforderungen erfüllen:

1. **Leerer String:** Ein leerer String `""` ergibt `0`.  
2. **Eine Zahl:** Ein String mit einer einzelnen Zahl gibt diese Zahl zurück.  
3. **Mehrere Zahlen:** Zahlen, die durch Kommas getrennt sind, werden addiert. Beispiel: `"1,2,3"` ergibt `6`.  
4. **Zeilenumbruch als Trenner:** Neben Kommas darf auch der Zeilenumbruch `\n` als Trennzeichen verwendet werden. Beispiel: `"1\n2,3"` ergibt `6`.  
5. **Benutzerdefinierter Trenner:** Der Benutzer kann einen eigenen Trenner definieren, z. B. `"//;\n1;2"` ergibt `3`.  
6. **Negative Zahlen:** Wenn negative Zahlen im String vorkommen, soll ein `ValueError` ausgelöst werden, der alle negativen Werte nennt.  
7. **Zahlen größer als 1000:** Zahlen, die größer als 1000 sind, werden ignoriert. Beispiel: `"2,1001"` ergibt `2`.  
8. **Trenner beliebiger Länge:** Der Trenner kann beliebig lang sein, z. B. `"//[***]\n1***2***3"` ergibt `6`.  
9. **Mehrere Trenner:** Es können mehrere verschiedene Trenner definiert werden, z. B. `"//[*][%]\n1*2%3"` ergibt `6`.

---

## Hinweise

- Achte darauf, dass dein Code übersichtlich und gut strukturiert bleibt.
- Denke daran, dass das Ziel nicht nur die korrekte Funktion, sondern auch die Qualität des Codes ist.

Viel Erfolg bei der Übung!