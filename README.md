# RTR105
<h1>Datormācība</h1>
<b>firefox<b>- atvēr pārlukprogrammu firefox<br>
uname -r - parāda operētājsistēmas kodols<br>
uname -a - izvada detalizētu informāciju par sistēmu<br>
history - parāda komandas vēsture<br>
echo $0 - parāda kads process tagad notiek.<br>
man uname - parāda komandās aprakstu<br>
man man - sniedz informāciju par citām komandām<br>
whoami - parāda lietotāja vārdu, kurš laiž komandas<br>
sh - lasa komandās no komandrinda<br>
who - parāda lietotāja vārds, kurš ir pieslēgts sistēmai<br>
pwd - parāda, kur es atrados<br>
ls - shell komanda, kura uzskaita failus un direktoriju direktorijas saturu.<br>
ls -l - Parāda kopejo failus skaitu direktorijā un apakšdirektorijā.<br>
ls -a - Saraksts ar failiem kurš satur visus failus un slēptas failus, kurie sākas ar '·'·<br>
ls -la - Garš saraksts ar slēptam failiem.<br>

ctrl+shift+t - new tab<br>
cd .. - atgrizties atpakaļ<br>
cd Music/ - nomainit direktoriju, piemēram uz mūziku.<br>
cd ~/ + x2 TAB - pāriet uz home direktoriju /home/user<br>
mkdir ManaMapa - uztaīsit jaunu mape<br>
rmdir ManaMape - dzēst mape<br>
ctrl + l - pabidīnat tekstu uz augšu<br>
echo - izvadīt tekstu<br>
echo "Teksts" > fails1.txt - uzrakstīt kaut kas failā<br>
cat fails1.txt - faila saturs<br>
echo "Teksts" >> fails1.txt - papildīnat failu<br>

rwx rwx rwx<br>
__ ___  ___<br>
000 000 000<br>
100 000 000<br>
 4   0   0<br>
 
 chmod 400 fails1.txt<br>
 chmod 700 fails1.txt<br>
 echo "Teksts" > ../fails1.txt<br>
 nano fails1.txt - teksta redaktors<br>
 cp fails1.txt fails3.txt - kopē ar visiem tiesībam<br>
 mv *.txt Music/- pārvietot visus txt failus<br>
 mv *.txt ../ - pārvietot visus txt failus uz līmeņu augstak<br>
 mv fails1.txt fails31.txt - pārsaukt failu<br>
rm *3*.txt - dzēst visus failus, kur ir 3.<br>
