## run all of the scripts needed to make lipid density plots 
#takes input $1 number of repeats

for i in $(seq 1 $1)
do
echo "Processing MD$i"
cd MD$i

#first, fit the protein and output files for each lipid/the backbone

#next make plumed script
bash ~/Documents/Analysis-scripts/density_plots/make_plumed_script2.sh POPE > POPE_plumed_coordinates.sh
bash ~/Documents/Analysis-scripts/density_plots/make_plumed_script2.sh POPG > POPG_plumed_coordinates.sh
bash ~/Documents/Analysis-scripts/density_plots/make_plumed_script2.sh CARD > CARD_plumed_coordinates.sh
bash ~/Documents/Analysis-scripts/density_plots/make_plumed_script2.sh BB > BB_plumed_coordinates.sh

#edit last lines of lipid plumed scripts
sed -i "s/PRINT ,pos/PRINT ARG=pos/g" POPE_plumed_coordinates.sh
sed -i "s/PRINT ,pos/PRINT ARG=pos/g" POPG_plumed_coordinates.sh
sed -i "s/PRINT ,pos/PRINT ARG=pos/g" CARD_plumed_coordinates.sh

#run plumed driver to get positions
plumed driver --mf_xtc md-centre-skip-POPE.xtc --plumed POPE_plumed_coordinates.sh
plumed driver --mf_xtc md-centre-skip-POPG.xtc --plumed POPG_plumed_coordinates.sh
plumed driver --mf_xtc md-centre-skip-CARD.xtc --plumed CARD_plumed_coordinates.sh
plumed driver --mf_pdb md-centre-BB.pdb --plumed BB_plumed_coordinates.sh

#make density plots
#module purge
python ~/Documents/Analysis-scripts/density_plots/lipid-density-xy-new.py

rm ./bck*
rm ./#*

cd ../
done
