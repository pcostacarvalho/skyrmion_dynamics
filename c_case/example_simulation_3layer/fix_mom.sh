mv moment.PdFeIr11.out moment.PdFeIr11.old
head -n 7 restart.PdFeIr11.out > moment.PdFeIr11.out
more moment.PdFeIr11.old >> moment.PdFeIr11.out
rm moment.PdFeIr11.old
