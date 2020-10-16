# batch_segmentation


If you are using this code, please cite: http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8206372

@inproceedings{abelha2017learning, \
    title={Learning How a Tool Affords by Simulating 3D Models from the Web}, \
    author={Abelha Ferreira, Paulo and Guerin, Frank}, \
    booktitle={Proceedings of IEEE International Conference on Intelligent Robots and Systems (IROS 2017)}, \
    year={2017}, \
    organization={IEEE Press} \
}

Batch segmentation using CGAL Triangulated Surface Mesh Segmentation
https://doc.cgal.org/latest/Surface_mesh_segmentation/index.html

By Paulo A. FErreira

E-mail: p.a.ferreira@cs.bham.ac.uk

If using this repository in your own research, please e-mail me to cite my work (the paper to cite is yet to be published).

This repository is part of my PhD. It contains the code and files for batch segmentation of point clouds.

You require CGAL to run my code.
The easiest way is to run my script easy_install.sh. It will install CGAL and compile my code for you.

After installating and compiling you can run demo.sh ad it will segment the demo point cloud that goes with the repository.

My code accepts --help and --verbose. I hope this helps you.


Good segmenting! :) 


- Meiying: 
install CGAl lib with
```
sudo apt-get install libcgal-dev

```

install meshlab with

```
sudo apt-get install meshlab
```

Other method may be needed potentially:

```
sudo apt-get install libcanberra-gtk-module
```

To run it to segment the meshes(example):
```
./segment_meshes -i data_demo -o data_demo_segmented -z 2:1:8,0.1:0.1:0.7 -e ply --verbose
```
It sometimes throw a floating point exception in the cgal functions. I don't know why that happens. To process a batch of point cloud, it would be more efficient to set a small range of the point cloud first, like
```
./segment_meshes -i data_demo -o data_demo_segmented -z 2:1:2,0.1:0.1:0.1 -e ply --verbose
```
Make sure all the initial point cloud are good. And then run the full batch, so you can leave it over-night.

It is better not to handle the SIGFPE, as the program may be in a very unstable state. More information from here: <https://stackoverflow.com/questions/39431879/c-handle-signal-sigfpe-and-continue-execution>

Merge similar segments
"""
./remove_similar_segm -i data_demo_segmented -o data_demo_segmented_unique --verbose
"""
It occasionally throws segmentation fault. This is likely happened because the point cloud file generated in the previous step is not complete. Just delete that ply and rerun the first command.

Organize the segments (we implement this)
"""
python pointcloud_get_segments.py
"""

Build with 
"""
make
"""