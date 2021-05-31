from manim import *
import numpy as np

class Intro(ThreeDScene):
	def construct(self):
		t1 = MathTex(r"\text{Schwarz Lemma}").scale(0.8)\
			.to_edge(UP)\
			.set_color_by_gradient(BLUE, GREEN)

		under_title = Underline(t1,buff = 0.2, color = BLUE)

		t1.add(under_title)

		self.play(FadeInFrom(t1,DOWN))

		self.wait(6)

		t1A = MathTex(r"\text{Let} \ f : \mathbb{D} \to \mathbb{C} \ \text{be a}", r"\ \text{holomorphic map}", r"\ \text{such that}", color = GOLD_B).scale(0.6)\
			.next_to(t1,DOWN)\
			.to_corner(LEFT)

		self.play(Write(t1A))

		self.wait(6)

		t1B = MathTex(r"\text{(i)} \ \ | f(z) | \leq 1 \ \text{for all} \ z \in \mathbb{D},", color = RED_B).scale(0.6)\
			.next_to(t1A,DOWN)\
			.to_corner(LEFT)

		self.play(Write(t1B))

		self.wait(6)

		t1C = MathTex(r"\text{(ii)} \ f(0) = 0.", color = PINK).scale(0.6)\
			.next_to(t1B,DOWN)\
			.to_corner(LEFT)

		self.play(Write(t1C))

		self.wait(6)

		t1D = MathTex(r"\text{Then} \ | f(z) | \leq | z | \ \text{for all} \ z \in \mathbb{D}.", color = BLUE).scale(0.6)\
			.next_to(t1C,DOWN)\
			.to_corner(LEFT)

		self.play(Write(t1D))

		self.wait(6)

		frame_box1 = SurroundingRectangle(t1A[1], buff = 0.1, color = PURPLE)

		self.play(FadeIn(frame_box1))

		self.wait(6)

		t2 = MathTex(r"\text{A smooth function} \ f : \mathbb{D} \to \mathbb{C} \ \text{is holomorphic if}").scale(0.6)\
			.next_to(t1D,RIGHT)\
			.to_corner(RIGHT)\
			.shift(LEFT)

		

		t2A = MathTex(r"\overline{\partial} f = 0 ", color = YELLOW).scale(0.6)\
			.next_to(t2,DOWN)

		

		t2B = MathTex(r"\frac{\partial f}{\partial \overline{z}} =0 ", color = RED_B).scale(0.6)\
			.next_to(t2A,RIGHT)\
			.shift(DOWN*0.5+RIGHT)

		t2A_copy = t2A.copy() 

		t2A_copy2 = t2A.copy()

		

		t2C = MathTex(r"\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \hspace{0.5cm} \frac{\partial v}{\partial x} = - \frac{\partial u}{\partial y}", color = BLUE).scale(0.6)\
			.next_to(t2B,LEFT)\
			.shift(LEFT + DOWN*0.4)

		

		t2D = MathTex(r"\text{complex differentiability}", color = GOLD_B).scale(0.6)\
			.next_to(t2,DOWN)\
			.shift(DOWN*2)

		

		hol_group = VGroup(t2,t2A, t2A_copy, t2A_copy2, t2D)

		hol_rect = SurroundingRectangle(hol_group, buff = 0.3, color = PURPLE)

		self.play(Transform(frame_box1, hol_rect))

		self.wait(6)

		self.play(Write(t2))

		self.wait(6)

		self.play(Write(t2A))

		self.wait(6)

		self.play(Transform(t2A_copy, t2B))

		self.wait(6)

		self.play(Transform(t2A_copy2, t2C))

		self.wait(6)

		self.play(FadeInFrom(t2D,DOWN))

		self.wait(6)

		frame_box2 = SurroundingRectangle(t1B, buff = 0.1, color = GREEN)

		t3 = MathTex(r"f \ \text{maps the unit disk} \ \mathbb{D}").scale(0.6)\
			.to_corner(LEFT)\
			.shift(RIGHT + DOWN*0.5)

		t3A = MathTex(r"\text{to itself} \ f(\mathbb{D}) \subset \mathbb{D}.").scale(0.6)\
			.next_to(t3,DOWN)

		t3.add(t3A)

		t3_box = SurroundingRectangle(t3, buff = 0.1, color = GREEN)

		self.play(FadeIn(frame_box2))

		self.wait(6)

		self.play(Transform(frame_box2, t3_box))

		self.wait(6)

		self.play(Write(t3))

		self.wait(6)

		frame_box3 = SurroundingRectangle(t1D, color = ORANGE, buff = 0.1)

		self.play(FadeIn(frame_box3))

		self.wait(6)

		t4 = MathTex(r"f \ \text{is distance decreasing}.", color = YELLOW).scale(0.6)\
			.to_corner(LEFT)\
			.shift(DOWN*3 + RIGHT*2)

		t4_box = SurroundingRectangle(t4, color = ORANGE, buff = 0.1)

		self.play(Transform(frame_box3, t4_box))

		self.wait(6)

		self.play(Write(t4))

		self.wait(6)

		# full_rect = FullScreenRectangle()

		# full_rect.set_fill(BLACK, opacity=0.9)

		# self.play(FadeIn(full_rect))

		# self.wait(6)

		# re_axis_1 = Line([-6, 0, 0], [-1,0,0], color = RED_B)

		# re_label_1 = MathTex(r"\text{Re}(z)", color = GOLD_B).scale(0.5)\
		# 	.next_to(re_axis_1,RIGHT)\
		# 	.shift(UP*0.2)

		# im_axis_1 = Line([-3.5, -2,0], [-3.5,2,0], color = RED_B)

		# im_label_1 = MathTex(r"\text{Im}(z)", color = GOLD_B).scale(0.5)\
		# 	.next_to(im_axis_1, UP)\
		# 	.shift(RIGHT*0.2)

		# axis_1 = VGroup(re_axis_1, im_axis_1, re_label_1, im_label_1)

		# self.play(Write(axis_1))

		# self.wait(6)

		# re_axis_2 = Line([1, 0, 0], [6,0,0], color = RED_B)

		# re_label_2 = MathTex(r"\text{Re}(w)", color = GOLD_B).scale(0.5)\
		# 	.next_to(re_axis_2,RIGHT)\
		# 	.shift(UP*0.2)

		# im_axis_2 = Line([3.5, -2,0], [3.5,2,0], color = RED_B)

		# im_label_2 = MathTex(r"\text{Im}(w)", color = GOLD_B).scale(0.5)\
		# 	.next_to(im_axis_2, UP)\
		# 	.shift(RIGHT*0.2)

		# axis_2 = VGroup(re_axis_2, im_axis_2, re_label_2, im_label_2)

		# self.play(Write(axis_2))

		# self.wait(6)

		# disk_1 = Circle(arc_center = [-3.5,0,0], radius = 1.5, color = BLUE, fill_color = BLUE, fill_opacity = 0.7)

		# disk_1_center = Dot(point = [-3.5,0,0], color = YELLOW)

		# disk_1_label = MathTex(r"\mathbb{D}", color = BLUE).scale(0.7)\
		# 	.next_to(disk_1,DOWN)\
		# 	.shift(RIGHT*1.2+UP*0.5)

		# disk_1.add(disk_1_label)

		# self.play(Write(disk_1))

		# self.wait(6)

		# disk_2 = Circle(arc_center = [3.5,0,0], radius = 1.5, color = BLUE, fill_opacity = 0.7).set_color_by_gradient(BLUE, GREEN)

		# disk_2_label = MathTex(r"\mathbb{D}", color = GREEN).scale(0.7)\
		# 	.next_to(disk_2,DOWN)\
		# 	.shift(UP*0.5 + RIGHT*1.2)

		# disk_2.add(disk_2_label)

		# self.play(Write(disk_2))

		# self.wait(6)

		# disk_2_center = Dot(point = [3.5,0,0], color = YELLOW)

		# self.play(Write(disk_1_center), Write(disk_2_center))

		# self.wait(6)

		# hol_arc = CurvedArrow(start_point = [-1.2, 1.2,0], end_point = [1.8,1.2,0],angle = -PI/2, color = PINK)

		# hol_label = MathTex(r"f", color = PINK).scale(0.8)\
		# 	.next_to(hol_arc,UP)

		# hol_arc.add(hol_label)

		# self.play(Write(hol_arc))

		# self.wait(6)

		# dd2 = disk_2_center.copy()

		# self.play(Transform(disk_1_center, dd2))

		# self.wait(6)

		# disk_2_copy = disk_2.copy()

		# self.play(Transform(disk_1, disk_2_copy))

		# self.wait(6) # I don't like the way this transforms.

class MaximumPrinciple(Scene):
	def construct(self):

		t1 = MathTex(r"\text{The Maximum Principle}").scale(0.8)\
			.to_edge(UP)\
			.set_color_by_gradient(BLUE, GREEN)

		under_title = Underline(t1,buff = 0.2, color = BLUE)

		t1.add(under_title)

		self.play(FadeInFrom(t1,DOWN))

		self.wait(6)

		t1A = MathTex(r"\text{Let} \ \Omega \subset \mathbb{C} \ \text{be a bounded domain}.", color = GOLD_B).scale(0.6)\
			.next_to(t1,DOWN)\
			.to_corner(LEFT)

		self.play(Write(t1A))

		self.wait(6)

		t1B = MathTex(r"\text{Then for any holomorphic function} \ f \in \mathcal{O}(\Omega) \cap \mathcal{C}(\overline{\Omega}),", color = RED_B).scale(0.6)\
			.next_to(t1A,RIGHT)

		self.play(Write(t1B))

		self.wait(6)

		t1C = MathTex(r"\max_{z \in \overline{\Omega}} | f(z) | \ = \ \max_{z \in \partial \Omega} | f(z) |.", color = BLUE).scale(0.6)\
			.shift(UP*1.7)

		self.play(Write(t1C))

		self.wait(6)

		t1D = MathTex(r"\text{Here}, \ \mathcal{O}(\Omega) = \{ f : \Omega \to \mathbb{C} \ : \ f \ \text{is holomorphic} \ \}").scale(0.5)\
			.to_corner(DL)

		t1E = MathTex(r"\text{and} \ \mathcal{C}(\overline{\Omega}) = \{ f : \overline{\Omega} \to \mathbb{C} \ : \ f \ \text{is continuous} \ \}.").scale(0.5)\
			.next_to(t1D,RIGHT)

		self.play(Write(t1D))

		self.wait(6)

		self.play(Write(t1E))

		self.wait(6)

		t2 = MathTex(r"\text{Suppose} \ f \ \text{is non-constant},").scale(0.5)\
			.next_to(t1C,DOWN*1.5)\
			.to_corner(LEFT)\
			.shift(RIGHT*0.2)

		self.play(Write(t2))

		self.wait(6)

		t2A = MathTex(r"\ | f(z_0) | \geq | f(z) |,").scale(0.45)\
			.next_to(t2,DOWN)

		self.play(Write(t2A))

		self.wait(6)

		t2B = MathTex(r"\text{for some} \ z_0 \in \Omega \ \text{and all} \ z \in \mathbb{D}(z_0, r).").scale(0.4)\
			.next_to(t2A,DOWN)

		self.play(Write(t2B), FadeOut(t1D), FadeOut(t1E))

		self.wait(6)

		t2C = MathTex(r"\text{By the open mapping theorem},", color = GOLD_B).scale(0.5)\
			.next_to(t2B,DOWN*2)\
			.to_corner(LEFT)\
			.shift(DOWN*0.5 + RIGHT*0.5)

		self.play(Write(t2C))

		self.wait(6)

		t2D = MathTex(r"f(\mathbb{D}(z_0, r)) \subset \mathbb{C} \ \text{is open}.", color = GOLD_B).scale(0.5)\
			.next_to(t2C,DOWN)

		self.play(Write(t2D))

		self.wait(6)

		re_axis_2 = Line([-1, -3, 0], [5,-3,0], color = GOLD_B)

		re_label_2 = MathTex(r"\text{Re}(w)", color = GOLD_B).scale(0.5)\
			.next_to(re_axis_2,RIGHT)\
			.shift(UP*0.2)

		im_axis_2 = Line([-0.5, -3.5,0], [-0.5,0,0], color = GOLD_B)

		im_label_2 = MathTex(r"\text{Im}(w)", color = GOLD_B).scale(0.5)\
			.next_to(im_axis_2, UP)\
			.shift(RIGHT*0.2)

		axis_2 = VGroup(re_axis_2, im_axis_2, re_label_2, im_label_2)

		self.play(Write(axis_2))

		self.wait(6)

		pts = [[0, -2.5,0], [1,-2.7,0], [2,-2.8,0], [3,-2.7,0], [4,-2.5,0], [4.5,-1.5,0], [4,-0.8,0], [3.2,0.3,0],  [2.5,-1.5,0], [-0.1,0.5,0]]

		rounded_1 = Polygon(*pts, stroke_color=BLUE).round_corners(radius=0.6)

		Dom_label = MathTex(r"f(\mathbb{D}(z_0, r))", color = BLUE).scale(0.5)\
			.next_to(rounded_1,RIGHT)

		rounded_1.add(Dom_label)

		self.play(FadeIn(rounded_1))

		self.wait(6)

		f_dot = Dot(point = [0.9, -1.5, 0], color = ORANGE).scale(0.5)
		f_label = MathTex(r"f(z_0)", color = ORANGE).scale(0.4)\
			.next_to(f_dot, RIGHT)\
			.shift(DOWN*0.2 + LEFT*0.2)

		self.play(Write(f_dot), Write(f_label))

		self.wait(6)

		nbd = Circle(radius = 0.7, color = RED_B).move_to(f_dot)

		self.play(Write(nbd))

		self.wait(6)

		l1 = Line([-0.5,-3,0], [0.9,-1.5,0], color = PINK)

		self.play(Write(l1))

		self.wait(6)

		l1_length = MathTex(r"\text{length}  \ = \ | f(z_0) | ", color = PINK).scale(0.5)\
			.next_to(l1,RIGHT)\
			.to_edge(DOWN)

		l1_arrow = CurvedArrow([1,-3.5,0], [0.2, -2.25,0], color = PINK, angle = -PI/6).scale(0.8)

		self.play(Write(l1_length), Write(l1_arrow))

		self.wait(6)

		self.play(Indicate(nbd))

		self.wait(6)

		dot2 = Dot(point = [1.1, -1.3,0], color = GREEN).scale(0.5)

		dot2_label = MathTex(r"f(z_1)", color = GREEN).scale(0.4)\
			.next_to(dot2, UP+LEFT)\
			.shift(DOWN*0.3 + RIGHT*0.2)

		self.play(Write(dot2), Write(dot2_label), FadeOut(l1_length), FadeOut(l1_arrow))

		self.wait(6)

		l2 = Line([-0.5,-3,0], [1.1,-1.3,0], color = PINK)

		self.play(Write(l2))

		self.wait(6)

		gp = VGroup(dot2.copy(), dot2_label.copy())

		contra = MathTex(r"\implies | f(z_1) | > | f(z_0) |", color = GREEN).scale(0.6)\
			.shift(UP+RIGHT*3)

		self.play(Transform(gp,contra))

		self.wait(6)

		self.play(Indicate(t2A))

		self.wait(6)


class OpenMapping(Scene):
	def construct(self):

		t1 = MathTex(r"\text{The Open Mapping Theorem}").scale(0.8)\
			.to_edge(UP)\
			.set_color_by_gradient(BLUE, GREEN)

		under_title = Underline(t1,buff = 0.2, color = BLUE)

		t1.add(under_title)

		self.play(FadeInFrom(t1,DOWN))

		self.wait(6)

		t1A = MathTex(r"\text{If} \ f : \Omega \to \mathbb{C} \ \text{is holomorphic}.", color = GOLD_B).scale(0.6)\
			.next_to(t1,DOWN)\
			.to_corner(LEFT)

		self.play(Write(t1A))

		self.wait(6)

		t1B = MathTex(r"\text{Then} \ f \ \text{is an open map}.", color = GOLD_B).scale(0.6)\
			.next_to(t1A,RIGHT)

		self.play(Write(t1B))

		self.wait(6)

		t1C = MathTex(r"\text{If} \ U \ \text{is an open set}", color = RED_B).scale(0.6)\
			.shift(UP*2 + LEFT*5)

		t1D = MathTex(r"\ \implies \ f(U) \ \text{is an open set}.", color = RED_B).scale(0.6)\
			.next_to(t1C,RIGHT)

		self.play(Write(t1C))

		self.wait(6)

		self.play(Write(t1D))

		self.wait(6)

		t2 = MathTex(r"\text{Open maps are special:}", color = PINK).scale(0.6)\
			.next_to(t1D,DOWN)\
			.to_corner(LEFT)\
			.shift(DOWN)

		self.play(Write(t2))

		self.wait(6)

		t2A = MathTex(r"f : \mathbb{R} \to \mathbb{R}, \ f(x) = 1,", color = PURPLE).scale(0.6)\
			.next_to(t2,RIGHT)

		self.play(Write(t2A))

		self.wait(6)

		t2B = MathTex(r"f(\mathbb{R}) = \{ 1 \}", color = GREEN).scale(0.6)\
			.next_to(t2A,RIGHT)

		self.play(Write(t2B))

		self.wait(6)

class Proof(Scene):
	def construct(self):
		t1 = MathTex(r"\text{Schwarz Lemma}").scale(0.8)\
			.to_edge(UP)\
			.set_color_by_gradient(BLUE, GREEN)

		under_title = Underline(t1,buff = 0.2, color = BLUE)

		t1.add(under_title)

		self.play(FadeInFrom(t1,DOWN))

		self.wait(6)

		t1A = MathTex(r"\text{Let} \ f : \mathbb{D} \to \mathbb{C} \ \text{be a}", r"\ \text{holomorphic map}", r"\ \text{such that}", color = GOLD_B).scale(0.6)\
			.next_to(t1,DOWN)\
			.to_corner(LEFT)

		self.play(Write(t1A))

		self.wait(6)

		t1B = MathTex(r"\text{(i)} \ \ | f(z) | \leq 1 \ \text{for all} \ z \in \mathbb{D},", color = RED_B).scale(0.6)\
			.next_to(t1A,DOWN)\
			.to_corner(LEFT)

		self.play(Write(t1B))

		self.wait(6)

		t1C = MathTex(r"\text{(ii)} \ f(0) = 0.", color = PINK).scale(0.6)\
			.next_to(t1B,RIGHT)

		self.play(Write(t1C))

		self.wait(6)

		t1D = MathTex(r"\text{Then} \ | f(z) | \leq | z | \ \text{for all} \ z \in \mathbb{D}.", color = BLUE).scale(0.6)\
			.next_to(t1C,DOWN)\
			.to_corner(LEFT)

		self.play(Write(t1D))

		self.wait(6)

		p1 = MathTex(r"\text{Proof:}").scale(0.6)\
			.next_to(t1D,DOWN)\
			.to_corner(LEFT)\
			.shift(DOWN)

		self.play(Write(p1))

		self.wait(6)

		p2 = MathTex(r"\text{Consider} \ g(z) : = \frac{f(z)}{z},", color = GOLD_B).scale(0.6)\
			.next_to(p1,RIGHT)

		self.play(Write(p2))

		self.wait(6)

		p2A = MathTex(r"\text{for} \ z \in \mathbb{D} - \{ 0 \}.", color = GOLD_B).scale(0.6)\
			.next_to(p2,RIGHT)

		self.play(Write(p2A))

		self.wait(6)

		p2B = MathTex(r"\text{Setting} \ g(0) : = f'(0),", color = GREEN).scale(0.6)\
			.next_to(p2A,DOWN)\
			.to_corner(LEFT)

		self.play(Write(p2B))

		self.wait(6)

		p2C = MathTex(r"\text{we get a holomorphic function} \ g : \mathbb{D} \to \mathbb{C}.", color = GREEN).scale(0.6)\
			.next_to(p2B,RIGHT)

		self.play(Write(p2C))

		self.wait(6)

		p3 = MathTex(r"\text{Fix some} \ z_0 \in \mathbb{D},", color = BLUE).scale(0.6)\
			.next_to(p2C,DOWN)\
			.to_corner(LEFT)

		self.play(Write(p3))

		self.wait(6)

		p3A = MathTex(r"\text{and choose} \ | z_0 | < r < 1.", color = BLUE).scale(0.6)\
			.next_to(p3,RIGHT)

		self.play(Write(p3A))

		self.wait(6)

		p4 = MathTex(r"\text{By the maximum principle:}", color = RED_B).scale(0.6)\
			.next_to(p3A,RIGHT)

		self.play(Write(p4))

		self.wait(6)

		p4A = MathTex(r"|g(z_0) | \leq \max_{| z | =r} | g(z) |", color = YELLOW).scale(0.6)\
			.next_to(p4,DOWN)\
			.to_corner(LEFT)\
			.shift(RIGHT*2+DOWN*0.2)

		self.play(Write(p4A))

		self.wait(6)

		p4B = MathTex(r"= \max_{| z | =r} \left | f(z)/z \right|", color = YELLOW).scale(0.6)\
			.next_to(p4A,RIGHT)

		self.play(Write(p4B))

		self.wait(6)

		p4C = MathTex(r"\leq \frac{1}{r}", color = YELLOW).scale(0.6)\
			.next_to(p4B,RIGHT)

		self.play(Write(p4C))

		self.wait(6)

		p4D = MathTex(r"\to 1, \hspace{1cm} \ \text{as} \ r \to 1.", color = YELLOW).scale(0.6)\
			.next_to(p4C,RIGHT)

		self.play(Write(p4D))

		self.wait(6)

		p_group = VGroup(p4A.copy(), p4B.copy(), p4C.copy(), p4D.copy())

		p5 = MathTex(r"|g(z_0) | \leq 1", color = ORANGE).scale(0.6)\
			.next_to(p4B,DOWN)\
			.shift(DOWN*0.2)

		self.play(Transform(p_group, p5))

		self.wait(6)

		p5A = MathTex(r"| f(z_0) | \leq | z_0 |", color = ORANGE).scale(0.6)\
			.next_to(p4B,DOWN)\
			.shift(DOWN*0.2)

		self.play(Transform(p_group, p5A))

		self.wait(6)

class Liouville(Scene):
	def construct(self):

		t1 = MathTex(r"\text{Applications of the Schwarz Lemma}").scale(0.8)\
			.to_edge(UP)\
			.set_color_by_gradient(BLUE, GREEN)

		under_title = Underline(t1,buff = 0.2, color = BLUE)

		t1.add(under_title)

		self.play(FadeInFrom(t1,DOWN))

		self.wait(6)

		t1A = MathTex(r"\text{Let} \ f : \mathbb{D}(R_1) \to \mathbb{D}(R_2) \ \text{be holomorphic},", color = GOLD_B).scale(0.6)\
			.next_to(t1,DOWN)\
			.to_corner(LEFT)

		self.play(Write(t1A))

		self.wait(6)

		t1B = MathTex(r"\text{with} \ f(0) = 0.", color = GOLD_B).scale(0.6)\
			.next_to(t1A,RIGHT)

		self.play(Write(t1B))

		self.wait(6)

		t1C = MathTex(r"\text{Then} \ f(z/R_1) : \mathbb{D} \to \mathbb{D}(R_2) \ \text{is holomorphic},", color = RED_B).scale(0.6)\
			.next_to(t1B,DOWN)\
			.to_corner(LEFT)

		self.play(Write(t1C))

		self.wait(6)

		t1D = MathTex(r"\text{and} \ \frac{1}{R_2} f(z/R_1) : \mathbb{D} \to \mathbb{D} \ \text{is holomorphic}.", color = PINK).scale(0.6)\
			.next_to(t1C,RIGHT)

		self.play(Write(t1D))

		self.wait(6)

		t2 = MathTex(r"\text{Schwarz lemma}", color = BLUE).scale(0.6)\
			.next_to(t1D,DOWN)\
			.to_corner(LEFT)\
			.shift(DOWN*0.2 + RIGHT*1.5)

		self.play(Write(t2))

		self.wait(6)

		t2A = MathTex(r"\ \implies \ ", color = BLUE).scale(0.6)\
			.next_to(t2,RIGHT)

		self.play(Write(t2A))

		self.wait(6)

		t2B = MathTex(r"| f(z/R_1) / R_2 | \leq | z | ", color = BLUE).scale(0.6)\
			.next_to(t2A,RIGHT)

		self.play(Write(t2B))

		self.wait(6)

		t2C = MathTex(r"\ \implies \ | f(z) | \leq \frac{R_2}{R_1} | z |", color = BLUE).scale(0.6)\
			.next_to(t2B,RIGHT)

		self.play(Write(t2C))

		self.wait(6)

		t3 = MathTex(r"\text{Suppose} \ f : \mathbb{C} \to \mathbb{C} \ \text{is entire}.", color = YELLOW).scale(0.6)\
			.next_to(t2C,DOWN)\
			.to_corner(LEFT)\
			.shift(DOWN*0.5)

		self.play(Write(t3))

		self.wait(6)

		t3A = MathTex(r"\text{Then for any} \ R_1, R_2 > 0,", color = RED_B).scale(0.6)\
			.next_to(t3,RIGHT)

		self.play(Write(t3A))

		self.wait(6)

		t3B = MathTex(r"\text{such that} \ f : \mathbb{D}(R_1) \to \mathbb{D}(R_2),", color = RED_B).scale(0.6)\
			.next_to(t3A,RIGHT)

		self.play(Write(t3B))

		self.wait(6)

		t3C = MathTex(r"| f(z) | \leq \frac{R_2}{R_1} | z |", color = BLUE).scale(0.6)\
			.next_to(t3B,DOWN)\
			.to_corner(LEFT)\
			.shift(RIGHT*4)

		self.play(Write(t3C))

		self.wait(6)

		t3D = MathTex(r"\to 0, \ \ \  \text{as} \ R_1 \to \infty.", color = BLUE).scale(0.6)\
			.next_to(t3C,RIGHT)

		self.play(Write(t3D))

		self.wait(6)

		t4 = MathTex(r"\text{Liouville Theorem}").scale(0.8)\
			.to_edge(DOWN)\
			.set_color_by_gradient(PINK, PURPLE)\
			.shift(UP*1.5)

		under_title2 = Underline(t4,buff = 0.2, color = PURPLE)

		t4.add(under_title2)

		self.play(FadeInFrom(t4,DOWN))

		self.wait(6)

		t4A  = MathTex(r"\text{A bounded entire function is constant}.").scale(0.6)\
			.next_to(t4,DOWN)
			# .to_corner(LEFT)

		self.play(Write(t4A))

		self.wait(6)























