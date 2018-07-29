#!/bin/bash

password="password"
min_reached_flag=0

min_file_name="password.x.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.p.o.n.m.l.k.j.i.h.g.f.e.d.c.b.a.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.max"
while [ ! -f "/password" ]
do
    temp_min=$min_file_name
    for file in *
    do
        if [ ${file: -3} != "zip" ] && [ ${file: -2} != "sh" ] 
        then
            echo $file;
            new_size=${#file}
            echo $new_size
            min_size=${#min_file_name}
            if (( $new_size < $min_size ))
            then
                temp_min=$file
                echo $temp_min
            fi
        fi
    done
    if (( $min_reached_flag == 1 )) && [ $temp_min == $min_file_name ]
    then
        break
    else
        echo "Unzipping..."
        min_file_name=$temp_min
        unzip $min_file_name
    fi
done
