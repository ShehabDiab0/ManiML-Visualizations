from manim import *
import pandas as pd

# top_left_coord=[-5, 2.5, 0]

def create_mat(A, label):
    A_mob = Matrix(A, left_bracket="(", right_bracket=")").scale(0.7)
    A_text = Text(label).scale(0.7).next_to(A_mob, UP)

    matrix_group = VGroup()
    matrix_group.add(A_mob, A_text)
    return matrix_group, A_mob



class VisualizeNumpy(Scene):
    def construct(self):
        top_left=[-5, 2.5, 0]
        
        A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        A_group, A_mob = create_mat(A, "Matrix A")

        self.play(Create(A_group.move_to(top_left)))
        self.wait(2)

        diag_A = np.diag(A).reshape(-1, 1)
        diag_group_A, _ = create_mat(diag_A, "Extracted Diagonal (np.diag(A))")

        self.play(A_group.animate.move_to(top_left), Create(diag_group_A))
        self.wait(2)

        constructed_diag_A = np.diag(np.diag(A))
        construct_diag_group, _ = create_mat(constructed_diag_A, "Construct from Diagonal (np.diag(np.diag(A)))")
        # construct_diag_mob.to_corner(top_left)
        
        self.play(Transform(diag_group_A, construct_diag_group))
        self.wait(2)
        self.play(FadeOut(diag_group_A))

        A = np.arange(12).reshape((4, 3))
        new_A_group, _ = create_mat(A, "Matrix A")
        self.play(Transform(A_group, new_A_group.move_to(top_left)))

        B = np.arange(3).reshape((1, 3))
        B_group, B_mob = create_mat(B, "Matrix B")
        B_mob2 = Matrix(B, left_bracket="(", right_bracket=")").scale(0.7)
        B_mob3 = Matrix(B, left_bracket="(", right_bracket=")").scale(0.7)
        B_mob4 = Matrix(B, left_bracket="(", right_bracket=")").scale(0.7)
        self.play(Create(B_group.next_to(new_A_group, DOWN)),
                  Create(B_mob2.move_to(B_mob.get_center())),
                  Create(B_mob3.move_to(B_mob.get_center())),
                  Create(B_mob4.move_to(B_mob.get_center())))

        self.play(B_mob2.animate.move_to(B_mob).shift([0, -0.5, 0]))
        self.play(B_mob3.animate.move_to(B_mob2).shift([0, -0.5, 0]))
        self.play(B_mob4.animate.move_to(B_mob3).shift([0.0, -0.5, 0.0]))

        all_b_entries = np.vstack([B, B, B, B])

        broadcasting_B, _ = create_mat(all_b_entries, "B for Broadcasting")
        broadcasting_B.next_to(new_A_group, DOWN)
        
        self.play(
            Transform(B_group, broadcasting_B, run_time=1.5),
            Transform(B_mob2, broadcasting_B, run_time=1.5),
            Transform(B_mob3, broadcasting_B, run_time=1.5),
            Transform(B_mob4, broadcasting_B, run_time=1.5),
        )
        self.wait(2)

        a_b_sum = A + B
        sum_mob, _ = create_mat(a_b_sum, "A + B (Done with broadcasting)")

        self.play(FadeOut(B_group, B_mob2, B_mob3, B_mob4, run_time=0.00001), Transform(A_group, sum_mob, run_time=3), Transform(broadcasting_B, sum_mob, run_time=3))
        self.wait(2)

        self.play(FadeOut(broadcasting_B, A_group))
        
        # Stacking arrays
        A = np.arange(3).reshape((3, 1))
        B = np.arange(3, 6).reshape((3, 1))
        
        A_group, A_mob = create_mat(A, "Matrix A")
        A_mob2 = Matrix(A, left_bracket="(", right_bracket=")").scale(0.7)
        A_mob3 = Matrix(A, left_bracket="(", right_bracket=")").scale(0.7)

        B_group, B_mob = create_mat(B, "Matrix B")
        B_mob2 = Matrix(B, left_bracket="(", right_bracket=")").scale(0.7).next_to(A_mob2, DOWN)
        B_mob3 = Matrix(B, left_bracket="(", right_bracket=")").scale(0.7).next_to(A_mob2, DOWN)

        A_group.move_to(top_left)
        A_mob2.move_to(A_mob.get_center())
        A_mob3.move_to(A_mob.get_center())
        
        B_group.next_to(A_group, DOWN)
        B_mob2.move_to(B_mob.get_center())
        B_mob3.move_to(B_mob.get_center())

        self.play(Create(A_group), Create(B_group), Create(A_mob2), 
                  Create(A_mob3), Create(B_mob2), Create(B_mob3))
        self.wait(2)

        

        # Vertical stacking
        self.play(A_mob2.animate.move_to(ORIGIN))
        self.play(B_mob2.animate.next_to(A_mob2, DOWN))
        self.wait(1)

        A_B_vstack = np.vstack((A, B))
        vstack_group, _ = create_mat(A_B_vstack, "Vertical Stacking np.vstack((a, b))")
        self.play(FadeTransform(A_mob2, vstack_group), FadeTransform(B_mob2, vstack_group))
        self.wait(1)
        self.play(FadeOut(vstack_group))
        

        # Horizontal stacking
        A_B_hstack = np.hstack((A, B))
        hstack_group, _ = create_mat(A_B_hstack, "Horizontal Stacking np.hstack((a, b))")
        self.play(A_mob3.animate.move_to(ORIGIN))
        self.play(B_mob3.animate.next_to(A_mob3, RIGHT))
        self.wait(1)

        self.play(FadeTransform(A_mob3, hstack_group), FadeTransform(B_mob3, hstack_group))
        self.wait(1)
        self.play(FadeOut(hstack_group, A_group, B_group, run_time=2))