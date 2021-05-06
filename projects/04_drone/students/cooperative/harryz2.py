import numpy as np

class RobotController:
    def __init__(self, limiter=None):
        self.dt = 0.01
        self.limiter = limiter
        self.A = np.array([[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, -0.0, 0.0, 0.0, 0.0, 1.0, -0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 9.81, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, -9.81, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, -0.0, -0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.0, -0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]])
        self.B = np.array([[0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, -0.0], [0.0, 0.0, 0.0, 2.0], [434.7826086956522, 0.0, 0.0, 0.0], [0.0, 434.7826086956522, 0.0, 0.0], [0.0, 0.0, 250.0, 0.0]])
        self.C = np.array([[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]])
        self.K = np.array([[-2.810080883993808e-15, -1.2613124477738022, 6.950467773612513e-16, 3.0503786429167423, -5.370324180369874e-15, -2.8143160095484697e-15, -1.0181589514046684e-15, -0.8941762802111444, -5.12842121407869e-16, 0.4593489291672664, -2.6651605894871407e-18, -2.888747514170912e-16], [0.7282190812544126, -3.28662799762878e-15, -1.9750243929025803e-16, 2.0543639551607953e-15, 2.6460048485695338, -9.78739991259383e-16, 0.6387407019518249, -1.4962044811496186e-15, 6.974363330988232e-17, -2.6651605894871407e-18, 0.45731971231635843, -7.364310600917789e-17], [-1.3307665136619746e-16, 1.0518079991734897e-16, 2.0216654119872858e-15, -1.77547408967219e-15, -9.447722252942977e-16, 1.1415035273840846, 1.7767668940701206e-16, 5.995565854374637e-16, 2.5422356445331517e-16, -1.6610298206482745e-16, -4.2344785955277285e-17, 0.4539842785700515], [3.142237099589623e-15, 2.116196348790621e-14, 10.24695076595958, -2.152173625642678e-14, 3.574858508385653e-15, 1.9117277236273755e-14, 1.4994789234393307e-15, 1.1144865850276374e-14, 3.3536473824717428, -1.5569886805942902e-16, 2.117416707288027e-17, 1.3423004203135041e-16]])
        self.L = np.array([[10.310943555899932, 0.0, 0.0, 0.0, 0.4838019379971687, 0.0], [0.0, 10.310943555899932, 0.0, -0.4838019379971687, 0.0, 0.0], [0.0, 0.0, 9.893863947922348, 0.0, 0.0, 0.0], [0.0, -0.4838019379971687, 0.0, 9.881988299121792, 0.0, 0.0], [0.4838019379971687, 0.0, 0.0, 0.0, 9.881988299121792, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 9.893863947922348], [13.274810664082066, 0.0, 0.0, 0.0, 9.685493643646506, 0.0], [0.0, 13.274810664082066, 0.0, -9.685493643646506, 0.0, 0.0], [0.0, 0.0, 8.944271909999152, 0.0, 0.0, 0.0], [0.0, -0.08388592165773212, 0.0, 8.943878529594848, 0.0, 0.0], [0.08388592165773212, 0.0, 0.0, 0.0, 8.943878529594848, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 8.944271909999152]])
        self.f_z_e = 4.905
        self.pos_vector = [2.875, 3.125, 3.125]
        self.ring = None
        self.before = None
        self.after = None
        self.target = None
        self.counter = 0
        self.wait = 0
        self.order = None
        self.spacing = 2

    def get_color(self):
        return np.random.rand(3,).tolist()

    def reset(self, pos):
        self.counter = 0
        self.order = None
        self.xhat = np.zeros((12, 1))
        
    def run(self, pos, rpy, pos_ring, is_last_ring, pos_others):
        
        if self.order is None:
            self.order = 0
            x_pos = pos[0]
            y_pos = pos[1]
            for pos_other in pos_others:
                x_other = pos_other[0]
                y_other = pos_other[1]
                if x_pos < x_other:
                    self.order += 1
                elif x_pos == x_other:
                    if y_pos < y_other:
                        self.order += 1
            self.wait = self.order * self.spacing / self.dt
        
        if self.counter > self.wait:
            if is_last_ring:
                if np.linalg.norm(pos_ring + np.array([0., 0., 1.25]) - pos) > 1.75:
                    pos_des = pos_ring + np.array([0., 0., 1.25])
                else:
                    pos_des = pos_ring
            else:
                pos_des = []
                if not np.array_equal(self.ring, pos_ring):
                    self.ring = pos_ring
                    self.before = pos_ring - np.array([2., 0., 0.])
                    self.after = pos_ring + np.array([2., 0., 0.])
                    self.target = self.before
                if pos[0] > pos_ring[0]:
                    self.target = self.before
                elif np.linalg.norm(self.target - pos) < 0.75:
                    self.target = self.after
                for i in range(0, pos.shape[0]):
                    if np.abs(self.target[i] - self.xhat[i, :].item()) > 0.5 or i == 0:
                        i_des = self.xhat[i, :].item() + self.pos_vector[i] * (self.target[i] - self.xhat[i, :].item()) / np.linalg.norm(self.target - self.xhat[0:3, :].T)
                    else:
                        i_des = self.target[i]
                    pos_des.append(i_des)
            x_des = np.block([[np.array(pos_des), np.zeros(9)]]).T
            u = -self.K @ (self.xhat - x_des)
            tau_x = u[0, 0]
            tau_y = u[1, 0]
            tau_z = u[2, 0]
            f_z = u[3, 0] + self.f_z_e
            if self.limiter is not None:
                tau_x, tau_y, tau_z, f_z = self.limiter(tau_x, tau_y, tau_z, f_z)
                u = np.array([[tau_x], [tau_y], [tau_z], [f_z - self.f_z_e]])
            y = np.block([[pos, rpy]]).T
            self.xhat += self.dt * (self.A @ self.xhat + self.B @ u - self.L @ (self.C @ self.xhat - y))
        else:
            self.counter += 1
            tau_x, tau_y, tau_z, f_z = 0., 0., 0., 0.
        return tau_x, tau_y, tau_z, f_z