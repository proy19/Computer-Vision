# Assignment 1 

## Part A : Fundamentals
1) I calibrated the camera in MATLAB. Outputs/Script shown in file `Priyangka_Roy_Camera_Calibration.pdf`

## Part B : MATLAB Prototyping 
2) To find real world dimensions, I used the MATLAB ginput() function. The code is shown in `Part_B`. 
To test my code, I measured the distance of the side of a remote object shown in `pic.jpeg`. 

## Part C : Application Development
3) No, it is not feasible. I ran the code (source: docs.luxonis.com) in files `depth_stereo_camera.py` and `rgb_mono_camera.py`, but it kept giving me errors and did not open the camera. 

4) Intrinsic Matrix from Part A 

   [ 1160.0469 +/- 11.1237    1158.5178 +/- 10.9550 ]
   [  547.6532 +/- 2.6145      358.7546 +/- 3.3394  ]
   [  0.1792 +/- 0.0126       -0.3098 +/- 0.0468  ]
   
   Intrinsic Matrix from Part C (source : docs.luxonis.com/en/latest/pages/calibration/) 
   
   [ 1042.0007 +/- 10.1824    1062.4316 +/- 11.8110 ]
   [  498.5199 +/- 2.1191      224.9145 +/- 2.4126  ]
   [  0.1621 +/- 0.0104       -0.2011 +/- 0.0389  ]
   





