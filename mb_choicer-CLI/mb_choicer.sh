#!/bin/bash
while true; do
echo "1-Native"
echo "2-Viking Conquest"
echo "3-Napolenic wars"
echo "4-Any mod"
read -p "Your choose:" your_choose
if [ $your_choose -eq 1 ]; 
then
	echo "Native" > /home/$USER/.mbwarband/last_module_warband
	/home/$USER/.steam/steam/steamapps/common/MountBlade\ Warband/./mb_warband.sh
elif [ $your_choose -eq 2 ];
then
        echo "Viking Conquest" > /home/$USER/.mbwarband/last_module_warband
        /home/$USER/.steam/steam/steamapps/common/MountBlade\ Warband/./mb_warband.sh
elif [ $your_choose -eq 3 ];
then 
	echo "Napoleonic Wars" > /home/$USER/.mbwarband/last_module_warband
	/home/$USER/.steam/steam/steamapps/common/MountBlade\ Warband/./mb_warband.sh	
elif [ $your_choose -eq 4 ];
then
	echo "Mod list, Native is pure"
	ls -l /home/$USER/.steam/steam/steamapps/common/MountBlade\ Warband/Modules
	read -p "Write mod folder: " choose
        echo "$choose" > /home/$USER/.mbwarband/last_module_warband
        /home/$USER/.steam/steam/steamapps/common/MountBlade\ Warband/./mb_warband.sh
else
	clear
fi
done
