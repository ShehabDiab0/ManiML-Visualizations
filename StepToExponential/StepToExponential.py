from manim import *

class StepToExponential(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-1, 6, 1],
            y_range=[-1, 3, 1],
            axis_config={"include_numbers": True},
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        step_function = axes.plot(
            lambda x: 1 if x <= 0 else 0, 
            x_range=[-1, 5],
            use_smoothing=False,
            color=RED
        )

        # Latex
        step_label = MathTex(r"f(x) = \begin{cases} 1 & x \geq 0 \\ 0 & x > 0 \end{cases}", color=RED)
        step_label.next_to(step_function, UP, buff=1)

        exp_function = axes.plot(
            lambda x: np.exp(-0.5 * x), 
            x_range=[-1, 5],
            color=GREEN
        )
        exp_label = MathTex("f(x) = e^{-0.5x}", color=GREEN)
        exp_label.next_to(exp_function, UP, buff=1)

        self.play(Create(axes), Write(axes_labels))
        self.play(Create(step_function), Write(step_label))
        self.wait(2)

        self.play(
            Transform(step_function, exp_function),
            Transform(step_label, exp_label),
            run_time=3
        )
        self.wait(2)