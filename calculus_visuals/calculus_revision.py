from manim import *

class QuadraticSlope(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 9, 1],
            axis_config={"color": BLUE},
            x_length=6,
            y_length=6
        ).add_coordinates()
        
        quadratic = axes.plot(lambda x: x**2, color=WHITE)
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        
        def get_tangent_line(x):
            point = axes.c2p(x, x**2)
            slope_value = 2 * x
            line_length = 1.5 + abs(slope_value) * 0.5
            tangent_line = TangentLine(
                quadratic, 
                alpha=(x + 3) / 6,
                length=line_length,
                color=RED
            )
            return tangent_line, slope_value

        info_text = Text(f"x: -3\nSlope: {-6}", font_size=24).to_corner(UP + RIGHT)

        self.play(
            Create(axes),
            Create(labels),
            Create(quadratic),
            Write(info_text)
        )
        
        tangent, slope_value = get_tangent_line(-3)
        self.play(Create(tangent))
        
        x_vals = np.arange(-3, 3, 0.2)
        for x in x_vals:
            new_tangent, slope_value = get_tangent_line(x)
            new_info_text = Text(f"x: {x:.2f}\nSlope: {slope_value:.2f}", font_size=24).to_corner(UP + RIGHT)
            
            self.play(
                Transform(tangent, new_tangent),
                Transform(info_text, new_info_text),
                run_time=0.2
            )

        explanation = Text(
            "Slope at any point (x, x²) = 2x",
            font_size=24
        ).to_corner(DOWN)
        self.play(Write(explanation))
        self.wait(2)
