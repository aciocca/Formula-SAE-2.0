import tkinter as tk 
import tkinter.font as Font
import tkinter.ttk as ttk
import GUI.globalstuff as globalstuff
import GUI.RealTime.Utils.helperTools as ht

def createTextTab(notebook):
    textvarFrame = tk.Frame(notebook, name = "tableView")
    textvarFrame.grid(row = 0, column = 0, sticky = "nsew")
    ht.configureMultipleColumns(textvarFrame, 2)
    ht.configureMultipleRows(textvarFrame, 2)
    tableviewIcon = tk.PhotoImage(file = "res/textmodeicon.gif")
    lab = tk.Label(image = tableviewIcon)
    lab.image = tableviewIcon # Brutto workaround al garbage collector, prendersi la tab è molto più difficile
    notebook.add(textvarFrame, text = "Text Mode", compound = tk.LEFT, image = tableviewIcon)
    return textvarFrame

def createEngineSection(textvarFrame, boldFont):
    engineLabelFrame = ttk.LabelFrame(textvarFrame, text = "Engine")
    engineLabelFrame.grid(column = 0, row = 0, sticky = "nsew")
    ht.configureMultipleColumns(engineLabelFrame, 4)
    ht.configureMultipleRows(engineLabelFrame, 6)
    populateEngineSection(engineLabelFrame, boldFont)

def populateEngineSection(engineLabelFrame, boldFont):
    # Creazione label con nome
    rpmLabel = tk.Label(engineLabelFrame, text = "RPM: ", font = boldFont)
    tpsLabel = tk.Label(engineLabelFrame, text = "TPS: ", font = boldFont)
    t_h20Label = tk.Label(engineLabelFrame, text = "H2O t: ", font = boldFont)
    t_airLabel = tk.Label(engineLabelFrame, text = "AIR t: ", font = boldFont)
    t_oilLabel = tk.Label(engineLabelFrame, text = "OIL t: ", font = boldFont)
    vbbLabel = tk.Label(engineLabelFrame, text = "Vbb: ", font = boldFont)
    lambda1_avgLabel = tk.Label(engineLabelFrame, text = "λ1 avg: ", font = boldFont)
    lambda1_rawLabel = tk.Label(engineLabelFrame, text = "λ1: ", font = boldFont)
    k_lambdaLabel = tk.Label(engineLabelFrame, text = "K λ: ", font = boldFont)
    inj_lowLabel = tk.Label(engineLabelFrame, text = "Inj L: ", font = boldFont)
    inj_highLabel = tk.Label(engineLabelFrame, text = "Inj H: ", font = boldFont)
    gearLabel = tk.Label(engineLabelFrame, text = "Gear: ", font = boldFont)
    # Creazione label con valore
    rpmValue = tk.Label(engineLabelFrame, textvariable = globalstuff.rpm, width = 6)
    tpsValue = tk.Label(engineLabelFrame, textvariable = globalstuff.tps, width = 6)
    t_h20Value = tk.Label(engineLabelFrame, textvariable = globalstuff.t_h20, width = 6)
    t_airValue = tk.Label(engineLabelFrame, textvariable = globalstuff.t_air, width = 6)
    t_oilValue = tk.Label(engineLabelFrame, textvariable = globalstuff.t_oil, width = 6)
    vbbValue = tk.Label(engineLabelFrame, textvariable = globalstuff.vbb, width = 6)
    lambda1_avgValue = tk.Label(engineLabelFrame, textvariable = globalstuff.lambda1_avg, width = 6)
    lambda1_rawValue = tk.Label(engineLabelFrame, textvariable = globalstuff.lambda1_raw, width = 6)
    k_lambdaValue = tk.Label(engineLabelFrame, textvariable = globalstuff.k_lambda1, width = 6)
    inj_lowValue = tk.Label(engineLabelFrame, textvariable = globalstuff.inj_low, width = 6)
    inj_highValue = tk.Label(engineLabelFrame, textvariable = globalstuff.inj_high, width = 6)
    gearValue = tk.Label(engineLabelFrame, textvariable = globalstuff.gear, width = 6)
    # Posizionamento label con nome
    rpmLabel.grid(column = 0, row = 0)
    tpsLabel.grid(column = 0, row = 1)
    t_h20Label.grid(column = 0, row = 2)
    t_airLabel.grid(column = 0, row = 3)
    t_oilLabel.grid(column = 0, row = 4)
    vbbLabel.grid(column = 0, row = 5)
    lambda1_avgLabel.grid(column = 2, row = 0)
    lambda1_rawLabel.grid(column = 2, row = 1)
    k_lambdaLabel.grid(column = 2, row = 2)
    inj_lowLabel.grid(column = 2, row = 3)
    inj_highLabel.grid(column = 2, row = 4)
    gearLabel.grid(column = 2, row = 5)
    # Posizionamento label con valore
    rpmValue.grid(column = 1, row = 0)
    tpsValue.grid(column = 1, row = 1)
    t_h20Value.grid(column = 1, row = 2)
    t_airValue.grid(column = 1, row = 3)
    t_oilValue.grid(column = 1, row = 4)
    vbbValue.grid(column = 1, row = 5)
    lambda1_avgValue.grid(column = 3, row = 0)
    lambda1_rawValue.grid(column = 3, row = 1)
    k_lambdaValue.grid(column = 3, row = 2)
    inj_lowValue.grid(column = 3, row = 3)
    inj_highValue.grid(column = 3, row = 4)
    gearValue.grid(column = 3, row = 5)

def createGPSSection(textvarFrame, boldFont):
    GPSSectionLabelFrame = ttk.LabelFrame(textvarFrame, text = "GPS")
    GPSSectionLabelFrame.grid(column = 0, row = 1, sticky = "nsew")
    ht.configureMultipleColumns(GPSSectionLabelFrame, 4)
    ht.configureMultipleRows(GPSSectionLabelFrame, 4)
    populateGPSSection(GPSSectionLabelFrame, boldFont)

def populateGPSSection(GPSSectionLabelFrame, boldFont):
    # Creazione label con nome
    n_sLabel = tk.Label(GPSSectionLabelFrame, text = "n_s", font = boldFont)
    e_wLabel = tk.Label(GPSSectionLabelFrame, text = "e_w", font = boldFont)
    fixQualityLabel = tk.Label(GPSSectionLabelFrame, text = "fixQuality", font = boldFont)
    n_satsLabel = tk.Label(GPSSectionLabelFrame, text = "n_sats", font = boldFont)
    hdopLabel = tk.Label(GPSSectionLabelFrame, text = "hdop", font = boldFont)
    latitudeLabel = tk.Label(GPSSectionLabelFrame, text = "latitude", font = boldFont)
    longitudeLabel = tk.Label(GPSSectionLabelFrame, text = "longitude", font = boldFont)
    velGPSLabel = tk.Label(GPSSectionLabelFrame, text = "velGPS", font = boldFont)
    # Creazione label con valore
    n_sValue = tk.Label(GPSSectionLabelFrame, textvariable = globalstuff.n_s, width = 6)
    e_wValue = tk.Label(GPSSectionLabelFrame, textvariable = globalstuff.e_w, width = 6)
    fixQualityValue = tk.Label(GPSSectionLabelFrame, textvariable = globalstuff.fixQuality, width = 6)
    n_satsValue = tk.Label(GPSSectionLabelFrame, textvariable = globalstuff.n_sats, width = 6)
    hdopValue = tk.Label(GPSSectionLabelFrame, textvariable = globalstuff.hdop, width = 6)
    latitudeValue = tk.Label(GPSSectionLabelFrame, textvariable = globalstuff.latitude, width = 6)
    longitudeValue = tk.Label(GPSSectionLabelFrame, textvariable = globalstuff.longitude, width = 6)
    velGPSValue = tk.Label(GPSSectionLabelFrame, textvariable = globalstuff.velGPS, width = 6)
    # Posizionamento label con nome
    n_sLabel.grid(column = 0, row = 0)
    e_wLabel.grid(column = 0, row = 1)
    fixQualityLabel.grid(column = 0, row = 2)
    n_satsLabel.grid(column = 0, row = 3)
    hdopLabel.grid(column = 2, row = 0)
    latitudeLabel.grid(column = 2, row = 1)
    longitudeLabel.grid(column = 2, row = 2)
    velGPSLabel.grid(column = 2, row = 3)
    # Posizionamento label con valore
    n_sValue.grid(column = 1, row = 0)
    e_wValue.grid(column = 1, row = 1)
    fixQualityValue.grid(column = 1, row = 2)
    n_satsValue.grid(column = 1, row = 3)
    hdopValue.grid(column = 3, row = 0)
    latitudeValue.grid(column = 3, row = 1)
    longitudeValue.grid(column = 3, row = 2)
    velGPSValue.grid(column = 3, row = 3)

def createWheelSection(textvarFrame, boldFont):
    wheelSectionLabelFrame = ttk.LabelFrame(textvarFrame, text = "Wheels")
    wheelSectionLabelFrame.grid(column = 1, row = 0, sticky = "nsew")
    ht.configureMultipleColumns(wheelSectionLabelFrame, 4)
    ht.configureMultipleRows(wheelSectionLabelFrame, 6)
    populateWheelSection(wheelSectionLabelFrame, boldFont)

def populateWheelSection(wheelSectionLabelFrame, boldFont):
    # Creazione label con nome
    vel_fsxLabel = tk.Label(wheelSectionLabelFrame, text = "Vel fsx: ", font = boldFont)
    vel_fdxLabel = tk.Label(wheelSectionLabelFrame, text = "Vel fdx: ", font = boldFont)
    vel_rsxLabel = tk.Label(wheelSectionLabelFrame, text = "Vel rsx: ", font = boldFont)
    vel_rdxLabel = tk.Label(wheelSectionLabelFrame, text = "Vel rdx: ", font = boldFont)
    pot_fdxLabel = tk.Label(wheelSectionLabelFrame, text = "Pot fdx: ", font = boldFont)
    pot_fsxLabel = tk.Label(wheelSectionLabelFrame, text = "Pot fsx: ", font = boldFont)
    pot_rdxLabel = tk.Label(wheelSectionLabelFrame, text = "Pot rdx: ", font = boldFont)
    pot_rsxLabel = tk.Label(wheelSectionLabelFrame, text = "Pot rsx: ", font = boldFont)
    potFAccuracyLabel = tk.Label(wheelSectionLabelFrame, text = "pFAcc: ", font = boldFont)
    potRAccuracyLabel = tk.Label(wheelSectionLabelFrame, text = "pRAcc: ", font = boldFont)
    steeringEncoderLabel = tk.Label(wheelSectionLabelFrame, text = "Steering: ", font = boldFont)
    # Creazione label con valore
    vel_fsxValue = tk.Label(wheelSectionLabelFrame, textvariable = globalstuff.vel_fsx, width = 6)
    vel_fdxValue = tk.Label(wheelSectionLabelFrame, textvariable = globalstuff.vel_fdx, width = 6)
    vel_rsxValue = tk.Label(wheelSectionLabelFrame, textvariable = globalstuff.vel_rsx, width = 6)
    vel_rdxValue = tk.Label(wheelSectionLabelFrame, textvariable = globalstuff.vel_rdx, width = 6)
    pot_fdxValue = tk.Label(wheelSectionLabelFrame, textvariable = globalstuff.pot_fdx, width = 6)
    pot_fsxValue = tk.Label(wheelSectionLabelFrame, textvariable = globalstuff.pot_fsx, width = 6)
    pot_rdxValue = tk.Label(wheelSectionLabelFrame, textvariable = globalstuff.pot_rdx, width = 6)
    pot_rsxValue = tk.Label(wheelSectionLabelFrame, textvariable = globalstuff.pot_rsx, width = 6)
    potFAccuracyValue = tk.Label(wheelSectionLabelFrame, textvariable = globalstuff.potFAccuracy, width = 6)
    potRAccuracyValue = tk.Label(wheelSectionLabelFrame, textvariable = globalstuff.potRAccuracy, width = 6)
    steeringEncoderValue = tk.Label(wheelSectionLabelFrame, textvariable = globalstuff.steeringEncoder, width = 6)
    # Posizionamento label con nome
    vel_fsxLabel.grid(column = 0, row = 0)
    vel_fdxLabel.grid(column = 0, row = 1)
    vel_rsxLabel.grid(column = 0, row = 2)
    vel_rdxLabel.grid(column = 0, row = 3)
    pot_fdxLabel.grid(column = 0, row = 4)
    pot_fsxLabel.grid(column = 0, row = 5)
    pot_rdxLabel.grid(column = 2, row = 0)
    pot_rsxLabel.grid(column = 2, row = 1)
    potFAccuracyLabel.grid(column = 2, row = 2)
    potRAccuracyLabel.grid(column = 2, row = 3)
    steeringEncoderLabel.grid(column = 2, row = 4)
    # Posizionamento label con valore
    vel_fsxValue.grid(column = 1, row = 0)
    vel_fdxValue.grid(column = 1, row = 1)
    vel_rsxValue.grid(column = 1, row = 2)
    vel_rdxValue.grid(column = 1, row = 3)
    pot_fdxValue.grid(column = 1, row = 4)
    pot_fsxValue.grid(column = 1, row = 5)
    pot_rdxValue.grid(column = 3, row = 0)
    pot_rsxValue.grid(column = 3, row = 1)
    potFAccuracyValue.grid(column = 3, row = 2)
    potRAccuracyValue.grid(column = 3, row = 3)
    steeringEncoderValue.grid(column = 3, row = 4)

def createGyroSection(textvarFrame, boldFont):
    gyroSectionLabelFrame = ttk.LabelFrame(textvarFrame, text = "Gyroscopes")
    gyroSectionLabelFrame.grid(column = 1, row = 1, sticky = "nsew")
    ht.configureMultipleColumns(gyroSectionLabelFrame, 4)
    ht.configureMultipleRows(gyroSectionLabelFrame, 3)
    populateGyroSection(gyroSectionLabelFrame, boldFont)

def populateGyroSection(gyroSectionLabelFrame, boldFont):
    # Creazione label con nome
    gyro_xLabel = tk.Label(gyroSectionLabelFrame, text = "gyro_x: ", font = boldFont)
    gyro_yLabel = tk.Label(gyroSectionLabelFrame, text = "gyro_y: ", font = boldFont)
    gyro_zLabel = tk.Label(gyroSectionLabelFrame, text = "gyro_z: ", font = boldFont)
    accel_xLabel = tk.Label(gyroSectionLabelFrame, text = "accel_x: ", font = boldFont)
    accel_yLabel = tk.Label(gyroSectionLabelFrame, text = "accel_y: ", font = boldFont)
    accel_zLabel = tk.Label(gyroSectionLabelFrame, text = "accel_z: ", font = boldFont)
    # Creazione label con valore
    gyro_xValue = tk.Label(gyroSectionLabelFrame, textvariable = globalstuff.gyro_x)
    gyro_yValue = tk.Label(gyroSectionLabelFrame, textvariable = globalstuff.gyro_y)
    gyro_zValue = tk.Label(gyroSectionLabelFrame, textvariable = globalstuff.gyro_z)
    accel_xValue = tk.Label(gyroSectionLabelFrame, textvariable = globalstuff.accel_x)
    accel_yValue = tk.Label(gyroSectionLabelFrame, textvariable = globalstuff.accel_y)
    accel_zValue = tk.Label(gyroSectionLabelFrame, textvariable = globalstuff.accel_z)
    # Posizionamento label con nome
    gyro_xLabel.grid(column = 0, row = 0)
    gyro_yLabel.grid(column = 0, row = 1)
    gyro_zLabel.grid(column = 0, row = 2)
    accel_xLabel.grid(column = 2, row = 0)
    accel_yLabel.grid(column = 2, row = 1)
    accel_zLabel.grid(column = 2, row = 2)
    # Posizionamento label con valore
    gyro_xValue.grid(column = 1, row = 0)
    gyro_yValue.grid(column = 1, row = 1)
    gyro_zValue.grid(column = 1, row = 2)
    accel_xValue.grid(column = 3, row = 0)
    accel_yValue.grid(column = 3, row = 1)
    accel_zValue.grid(column = 3, row = 2)

def populatetextvarFrame(textvarFrame):
    boldFont = Font.Font(weight = "bold", size = 12)
    createEngineSection(textvarFrame, boldFont)
    createGPSSection(textvarFrame, boldFont)
    createWheelSection(textvarFrame, boldFont)
    createGyroSection(textvarFrame, boldFont)
    
    