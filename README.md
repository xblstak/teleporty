# Teleporty – Simulácia stolovej hry

Simulátor stolovej hry Teleporty v jazyku Python pre 1 až 4 hráčov na hracej ploche rozmerov n×n.

## Čo hra robí

Hráči sa striedajú v hádzaní kockou a posúvajú figúrky po 2D hracej ploche. Cieľom je dostať figúrku presne na cieľové políčko. Na ploche sú náhodne rozmiestnené teleporty dvoch typov:
- **pozitívny teleport** – posúva figúrku vpred (označený veľkým písmenom)
- **negatívny teleport** – posúva figúrku vzad (označený malým písmenom)

Hráč musí pristáť na cieľovom políčku presne – ak hodí viac bodov, ako je vzdialenosť do cieľa, ťah sa nevykoná.

## Funkcionalita

- Generovanie hracej plochy rozmerov n×n (5 ≤ n ≤ 10) s náhodným rozmiestnením teleportov
- Pohyb figúrok po mriežke so striedaním smeru v každom riadku
- Kocka so špeciálnym pravidlom: hod čísla 6 znamená ďalší hod s pričítaním bodov
- Textová vizualizácia stavu hracej plochy po každom ťahu
- Podpora 1 až 4 hráčov

## Spustenie

Program sa opýta na veľkosť hracej plochy a počet hráčov, následne prebehne simulácia automaticky bez ďalších vstupov.
