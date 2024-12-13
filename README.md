# ManiML-Visualizations
Repo will contain visualizations for Most used ML Algorithms

## installation to run manim
1- You can follow the Manim installation from the [documentation](https://docs.manim.community/en/stable/installation.html) but we will walk through it together.

2- Install FFMPEG, in windows u can do that using:
```
winget install ffmpeg
```
3- Install [MiKTeX](https://miktex.org/download) or in console using the command: 
```
winget install MiKTeX.MiKTeX
```
4- Now go to any visualization directory and run the following command:
```
manim file.py SceneObject -pqm
```

Example in KNN directory
```
manim KNN.py KNNVisualization -pqm
```

> Warning: The video will take time to render depending on how complex is the visualization.