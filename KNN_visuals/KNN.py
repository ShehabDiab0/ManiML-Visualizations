from manim import *
import pandas as pd
import numpy as np


class KNNVisualization(MovingCameraScene):
    def construct(self):
        df = pd.DataFrame({
            'x': np.random.randint(-10, 10, size=100),
            'y': np.random.randint(-10, 10, size=100),
            'class': np.random.randint(0, 2, size=100)
        })
        
        class_colors = {0: RED, 1: BLUE}
        
        query_point = [np.random.randint(-10, 10), 
                       np.random.randint(-10, 10),
                       0]
        
        grid = NumberPlane(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            axis_config={"color": GREY},
            background_line_style={"stroke_color": BLUE_D, "stroke_width": 1, "stroke_opacity": 0.5}
        )
        self.play(Create(grid))
        
        points = VGroup()
        for _, row in df.iterrows():
            point = Dot(point=[row['x'], row['y'], 0], color=class_colors[row['class']])
            points.add(point)
        
        self.play(FadeIn(points))

        self.play(self.camera.frame.animate.move_to(query_point))
        self.wait()
        
        query_dot = Dot(point=query_point, color=YELLOW)
        self.play(FadeIn(query_dot))
        

        distance_lines = VGroup()
        for point in points:
            line = Line(query_dot.get_center(), point.get_center(), color=WHITE, stroke_width=2)
            distance_lines.add(line)
        
        self.play(Create(distance_lines), runtime=3)
        self.wait()
        
        k = np.random.choice([3, 5, 7, 9])
        df['distance'] = np.sqrt((df['x'] - query_point[0])**2 + (df['y'] - query_point[1])**2)
        nearest_neighbors = df.nsmallest(k, 'distance')
        
        nearest_lines = VGroup()
        for _, row in nearest_neighbors.iterrows():
            nearest_line = Line(query_dot.get_center(), [row['x'], row['y'], 0], color=GREEN, stroke_width=4)
            nearest_lines.add(nearest_line)
        
        self.play(Transform(distance_lines, nearest_lines))
        self.wait()
        
        majority_class = nearest_neighbors['class'].mode()[0]
        decision_text = Text(f"Classified as {'BLUE' if majority_class == 1 else 'RED'}", color=class_colors[majority_class]).scale(0.75).shift(UP * 3)
        
        self.play(Write(decision_text))
        self.wait()
        
        self.play(query_dot.animate.set_color(class_colors[majority_class]))
        self.wait()
        
        self.play(FadeOut(nearest_lines), FadeOut(distance_lines), FadeOut(decision_text), FadeOut(query_dot), FadeOut(points), FadeOut(grid))
