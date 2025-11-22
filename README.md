# ISOcalc - Calculator Toleranțe ISO (Python GUI)

![Python](https://img.shields.io/badge/Python-3.11.9-blue)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
![Status](https://img.shields.io/badge/Project-Active-brightgreen)

ISOcalc este o aplicație realizată exclusiv în Python care calculează **toleranțele dimensionale conform ISO 286**, incluzând:

- **Toleranța dimensională**
- **Abaterea superioară**
- **Abaterea inferioară**

Interfața este simplă și intuitivă, realizată complet local, fără conexiune la internet. Este utilă pentru ingineri și tehnicieni care verifică sau proiectează piese cu **arbori** și **alezaje**.

---

## Funcționalități

- Introducere **dimensiune nominală** [mm]
- Selectare tip: **Arbore** / **Alezaj**
- Selectare poziție toleranță: **a/A … zc/ZC**
- Selectare treaptă IT: **01 – 18**
- Calcul instant al:
  - Toleranței dimensionale [mm]
  - Abaterii superioare [mm]
  - Abaterii inferioare [mm]
- Buton **Reset**
- Validări inteligente, conform ISO, pentru:
  - dimensiuni invalide
  - combinații nepermise între toleranțe și dimensiuni
  - zone de toleranță necorespunzătoare tipului arbore/alezaj
- Doar Python standard

---

## Capturi de ecran - folderul screenshots

Capturile de ecran prezintă interfața și funcționalitățile aplicației ISOcalc:

1. `1_Default.jpg` – Interfața implicită la deschiderea aplicației
2. `2_Selectare_Arbore.jpg` – Selectarea tipului Arbore
3. `3_Selectare_Alezaj.jpg` – Selectarea tipului Alezaj
4. `4_Optiuni_Clasa_de_Toleranta.jpg` – Selectarea zonei de toleranță
5. `5_Optiuni_Treapta_IT.jpg` – Selectarea treptei IT
6. `6_Calculare.jpg` – Rezultatul calculului toleranțelor și abaterilor
7. `7_Reset.jpg` – Funcția Reset
8. `8_Consola.jpg` – Mesaje și informații în consolă

---

## Tehnologii utilizate

- **Python 3.11.9**
- **Tkinter (GUI)**
- **Math & Numpy pentru calcule interne**

---

## Logica internă a programului

1. Utilizatorul introduce dimensiunile și selecțiile din UI
2. Aplicația validează datele conform normelor impuse de ISO (limite, combinații zone/IT, valori numerice)
3. Determină intervalul dimensional și selectează valoarea standardizată a toleranței, conform SR EN 20 286 - 1:1997
4. Identifică abaterile fundamentale (în funcție de tip și zonă), iar apoi se folosesc valorile extrase din ISO
5. Calculează cel de-al doilea parametru, în funcție de care parametru este deja cunoscut, lucru decis la pasul anterior:
   - Abaterea_superioară (Abaterea_inferioară + Toleranța dimensională)
   - Abaterea_inferioară (Abatere_superioară - Toleranța_dimensională)
6. Afișează toate rezultatele în UI

---

## Structura proiectului

```
ISOcalc/
├─ ISOcalc.py
├─ README.md
└─ screenshots/
    ├─ 1_Default.jpg
    ...
    └─ 8_Consola.jpg
```

---

## Licență

Acest proiect este oferit liber spre utilizare și modificare.

---

## Contact

Pentru întrebări sau sugestii:
- manoledaniel2004@gmail.com
- https://www.linkedin.com/in/manoledaniel/
