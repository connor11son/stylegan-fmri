docker run --gpus 1 --ipc=host -it --rm -v `pwd`:/scratch \
-v /media/hdd5/connor/stylegan-dsets/:/scratch/datasets  \
--workdir /scratch -e HOME=/scratch --name stylegan stylegan3 bash 