def get_xyz(depth_map, intrinsic_matrix):
        intrinsic = np.array(intrinsic_matrix['intrinsic_matrix'])
        imat_dim = np.array(intrinsic_matrix['intrinsic_matrix_reference_dimensions'], ndmin=2)
        
        image_dim = np.array([depth_map.shape[1], depth_map.shape[0]], ndmin=2) 
        
        ratio = imat_dim / image_dim
        
        intrinsic /= np.hstack([ratio, np.ones([1, 1])])

        u = np.arange(depth_map.shape[1]).reshape((1, -1))
        v = np.arange(depth_map.shape[0]).reshape((-1, 1))
            
        x = (u - intrinsic[2][0]) * depth_map / intrinsic[0][0]
        y = (v - intrinsic[2][1]) * depth_map / intrinsic[1][1]

        xyz = np.stack([x, y, depth_map], axis=2)
            
        return xyz
