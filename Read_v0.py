# explanation of the wfm format from the begining
import struct
from ROOT import TCanvas, TGraph, TH1F
# 78 bytes for the waveform static file information:
#    2 bytes, either 0xF0F0 (PPC format) or 0x0F0F (Intel), to determine if bytes read from file needed to be swapped before processing.

filename = "w-w-2nd-ch1-1200v-longCable-2ms_ch1_20190502101025236"
file_wfm = filename + ".wfm"
file_root = filename +".root"
with open(file_wfm, "rb") as bfile:
    #read the first 2 bytes
    bfile.seek(0)
    print "Waveform static file information:"
    pCode = struct.unpack('H',bfile.read(2))
    print pCode[0]
    #read the next 8 bytes - version number - char[8]
    vNumber = bfile.read(8)
    print "version number ", vNumber
    #read the next 1 byte - number of digits in byte count
    ndbc = struct.unpack('c',bfile.read(1))
    print "number of digits in byte count", ndbc
    #read the next 4 bytes - number of bytes to the end of the file
    nbEOF = struct.unpack('i', bfile.read(4))
    print "number of bytes to EOF ", nbEOF[0]
    #read the next 1 byte - number of bytes per point
    nbPt = struct.unpack('c',bfile.read(1))
    print "number of bytes per point", nbPt
    #read the next 4 bytes - byte offset to begining of curve buffer
    bOffset1 = struct.unpack('i',bfile.read(4))
    print "byte offset to begining of curve buffer ", bOffset1[0]
    #read the next 4 bytes - horizontal zoom scale factor 
    horScalF = struct.unpack('i',bfile.read(4))
    print "horizontal scale zoom factor ", horScalF[0]
    #read the next 4 bytes - horizontal zoom position
    horZoomP = struct.unpack('f', bfile.read(4))
    print "horizontal zoom position ", horZoomP[0]
    #read the next 8 bytes - vertical zoom scale factor
    verScaF = struct.unpack('d', bfile.read(8))
    print "vertical scale zoom factor ", verScaF[0]
    #read the next 4 bytes - vertical zoom position
    verZoomP = struct.unpack('f', bfile.read(4))
    print "vertical zoom position", verZoomP[0]
    #read the next 32 bytes - waveform label - char[32]
    wfmLabel = bfile.read(32)
    print "Waveform label (user defined or ref waveform)", wfmLabel
    #read the next 4 bytes - number of FastFrams-1
    nbFF = struct.unpack('i', bfile.read(4))
    print "Number of FastFrams-1", nbFF[0]
    #read the next 2 bytes - size of the waveform header
    sizeWfmHead = struct.unpack('H', bfile.read(2))
    print "Size of the waveform header", sizeWfmHead[0]

    print ""

    print "waveform header:"
    #Reference file data
    typeWfmSet = struct.unpack('i',bfile.read(4))
    print "Type of waveform set (0:single waveform, 1:FastFrame)", typeWfmSet[0]
    WfmCnt = struct.unpack('i',bfile.read(4))
    print "Number of waveforms in the set", WfmCnt[0]
    AcqCnt = struct.unpack('l',bfile.read(8))
    print "Acquisition counter", AcqCnt[0]
    TransCnt = struct.unpack('l',bfile.read(8))
    print "Transaction counter", TransCnt[0]
    SlotID = struct.unpack('i',bfile.read(4)) #Not for use
    IsStaticFlag = struct.unpack('i',bfile.read(4))
    print "IsStaticFlag, static or live 0-reference; 1-waveform or math", IsStaticFlag[0]
    WfmUpdateSpecCnt = struct.unpack('i',bfile.read(4))
    print "WfmUpdateSpecCnt", WfmUpdateSpecCnt[0]
    ImpDimRefCnt = struct.unpack('i',bfile.read(4))
    print "ImpDimRefCnt",ImpDimRefCnt[0]
    ExpDimRefCnt = struct.unpack('i',bfile.read(4))
    print "ExpDimRefCnt",ExpDimRefCnt[0]
    DataType = struct.unpack('i',bfile.read(4))
    print "DataType",DataType[0]
    GenPurposeCnt = struct.unpack('l',bfile.read(8))
    print "GenPurposeCnt",GenPurposeCnt[0]
    AccuWfmCnt = struct.unpack('i',bfile.read(4))
    print "AccuWfmCnt",AccuWfmCnt[0]
    TarAccuCnt = struct.unpack('i',bfile.read(4))
    print "TarAccuCnt",TarAccuCnt[0]
    CurveCnt = struct.unpack('i',bfile.read(4))
    print "CurveCnt",CurveCnt[0]
    nbReqFastFrame = struct.unpack('i',bfile.read(4))
    print "nbReqFastFrame",nbReqFastFrame[0]
    nbAcqFastFrame = struct.unpack('i',bfile.read(4))
    print "Number of frames", nbAcqFastFrame[0]
    SummFrame = struct.unpack('h',bfile.read(2))
    print "SummFrame",SummFrame[0]
    PixMapDisFormat = struct.unpack('i',bfile.read(4))
    print "PixMapDisFormat",PixMapDisFormat[0]
    PixMapMax = struct.unpack('l',bfile.read(8))
    print "PixMapMax",PixMapMax[0]

    #Explicit Dimension 1 (Usually defines voltage axis) 
    #  Description info 100 bytes 
    #  User View Data 56 bytes
    #ExpDim1 = bfile.read(156)
    DimScale = struct.unpack('d',bfile.read(8))
    print "DimScale",DimScale[0]
    DimOffset = struct.unpack('d',bfile.read(8))
    print "DimOffset",DimOffset[0]
    DimSize = struct.unpack('i',bfile.read(4))
    print "DimSize",DimSize[0]
    ExtDimUnits = bfile.read(20)
    print "ExtDimUnits",ExtDimUnits[0]
    DimExtentMin = struct.unpack('d',bfile.read(8))
    print "DimExtentMin",DimExtentMin[0]
    DimExtentMax = struct.unpack('d',bfile.read(8))
    print "DimExtentMax",DimExtentMax[0]
    DimResolution = struct.unpack('d',bfile.read(8))
    print "DimResolution",DimResolution[0]
    DimRefPoint = struct.unpack('d',bfile.read(8))
    print "DimRefPoint",DimRefPoint[0]
    ExpDimFormat = struct.unpack('i',bfile.read(4))
    print "ExpDimFormat",ExpDimFormat[0]
    ExpDimStorageType = struct.unpack('i',bfile.read(4))
    print "ExpDimStorageType",ExpDimStorageType[0]
    ExpDimNvalue = struct.unpack('i',bfile.read(4))
    print "ExpDimNvalue",ExpDimNvalue[0]
    ExpDimOverRange = struct.unpack('i',bfile.read(4))
    print "ExpDimOverRange",ExpDimOverRange[0]
    ExpDimUnderRange = struct.unpack('i',bfile.read(4))
    print "ExpDimUnderRange",ExpDimUnderRange[0]
    ExpDimHighRange = struct.unpack('i',bfile.read(4))
    print "ExpDimHighRange",ExpDimHighRange[0]
    ExpDimLowRange = struct.unpack('i',bfile.read(4))
    print "ExpDimLowRange",ExpDimLowRange[0]
    ExpDimUserScale = struct.unpack('d',bfile.read(8))
    print "ExpDimUserScale",ExpDimUserScale[0]
    ExpDimUserUnits = bfile.read(20)
    print "ExpDimUserUnits",ExpDimUserUnits[0]
    ExpDimUserOffset = struct.unpack('d',bfile.read(8))
    print "ExpDimUserOffset",ExpDimUserOffset[0]
    ExpDimPointDensity = struct.unpack('d',bfile.read(8))
    print "ExpDimPointDensity",ExpDimPointDensity[0]
    ExpDimHRef = struct.unpack('d',bfile.read(8))
    print "ExpDimHRef",ExpDimHRef[0]
    ExpDimTrigDelay = struct.unpack('d',bfile.read(8))
    print "ExpDimTrigDelay",ExpDimTrigDelay[0]
    #Explicit Dimension 2 
    #  100 + 56 bytes again
    #ExpDim2 = bfile.read(156)
    ImpDimScale = struct.unpack('d',bfile.read(8))
    print "ImpDimScale",ImpDimScale[0]
    ImpDimOffset = struct.unpack('d',bfile.read(8))
    print "ImpDimOffset",ImpDimOffset[0]
    ImpDimSize = struct.unpack('i',bfile.read(4))
    print "ImpDimSize",ImpDimSize[0]
    ImpDimUnits = bfile.read(20)
    print "ImpDimUnits",ImpDimUnits[0]
    ImpDimExtentMin = struct.unpack('d',bfile.read(8))
    print "ImpDimExtentMin",ImpDimExtentMin[0]
    ImpDimExtentMax = struct.unpack('d',bfile.read(8))
    print "ImpDimExtentMax",ImpDimExtentMax[0]
    ImpDimRes = struct.unpack('d',bfile.read(8))
    print "ImpDimRes",ImpDimRes[0]
    ImpDimRefPoint = struct.unpack('d',bfile.read(8))
    print "ImpDimRefPoint",ImpDimRefPoint[0]
    ImpDimSpacing = struct.unpack('i',bfile.read(4))
    print "ImpDimSpacing",ImpDimSpacing[0]
    ImpDimUserScale = struct.unpack('d',bfile.read(8))
    print "ImpDimUserScale",ImpDimUserScale[0]
    ImpDimUserScale1 = struct.unpack('d',bfile.read(8))
    print "ImpDimUserScale1 (caution)",ImpDimUserScale1[0]
    ImpDimUserUnits = bfile.read(20)
    print "ImpDimUserUnits",ImpDimUserUnits[0]
    ImpDimUserOffset = struct.unpack('d',bfile.read(8))
    print "ImpDimUserOffset",ImpDimUserOffset[0]
    ImpDimPointDensity = struct.unpack('d',bfile.read(8))
    print "ImpDimPointDensity",ImpDimPointDensity[0]
    ImpDimPointDensity1 = struct.unpack('d',bfile.read(8))
    print "ImpDimPointDensity1 (caution)",ImpDimPointDensity1[0]
    ImpDimHRef = struct.unpack('d',bfile.read(8))
    print "ImpDimHRef",ImpDimHRef[0]
    ImpDimTrigDelay = struct.unpack('d',bfile.read(8))
    print "ImpDimTrigDelay",ImpDimTrigDelay[0]
    TimeBase_RealPointSpacing = struct.unpack('i',bfile.read(4))
    print "TimeBase_RealPointSpacing",TimeBase_RealPointSpacing[0]
    TimeBase_Sweep = struct.unpack('i',bfile.read(4))
    print "TimeBase_Sweep",TimeBase_Sweep[0]
    TimeBase_TypeBase = struct.unpack('I',bfile.read(4))
    print "TimeBase_TypeBase",TimeBase_TypeBase[0]
    
    WfmUpdaSpec_RealPointOffset = struct.unpack('i',bfile.read(4))
    print "WfmUpdaSpec_RealPointOffset",WfmUpdaSpec_RealPointOffset[0]
    WfmUpdaSpec_TTOffset = struct.unpack('d',bfile.read(8))
    print "WfmUpdaSpec_TTOffset",WfmUpdaSpec_TTOffset[0]
    WfmUpdaSpec_FracSec = struct.unpack('d',bfile.read(8))
    print "WfmUpdaSpec_FracSec",WfmUpdaSpec_FracSec[0]
    WfmUpdaSpec_GmtSec = struct.unpack('i',bfile.read(4))
    print "WfmUpdaSpec_GmtSec",WfmUpdaSpec_GmtSec[0]
    
    WfmCurveInfo_StateFlag = struct.unpack('i',bfile.read(4))
    print "WfmCurveInfo_StateFlag",WfmCurveInfo_StateFlag[0]
    WfmCurveInfo_TypeCheckSum = struct.unpack('i',bfile.read(4))
    print "WfmCurveInfo_TypeCheckSum",WfmCurveInfo_TypeCheckSum[0]
    WfmCurveInfo_CheckSum = struct.unpack('H',bfile.read(2))
    print "WfmCurveInfo_CheckSum",WfmCurveInfo_CheckSum[0]
    WfmCurveInfo_preQstartOffset = struct.unpack('i',bfile.read(4))
    print "WfmCurveInfo_preQstartOffset",WfmCurveInfo_preQstartOffset[0]
    WfmCurveInfo_dataStartOffset = struct.unpack('i',bfile.read(4))
    print "WfmCurveInfo_dataStartOffset",WfmCurveInfo_dataStartOffset[0]
    WfmCurveInfo_postQstartOffset = struct.unpack('i',bfile.read(4))
    print "WfmCurveInfo_postQstartOffset",WfmCurveInfo_postQstartOffset[0]
    WfmCurveInfo_postQStopOffset = struct.unpack('i',bfile.read(4))
    print "WfmCurveInfo_postQStopOffset",WfmCurveInfo_postQStopOffset[0]
    WfmCurveInfo_EOCoffset = struct.unpack('i',bfile.read(4))
    print "WfmCurveInfo_EOCoffset",WfmCurveInfo_EOCoffset[0]
    
    cCanvas = TCanvas()
    cCanvas.SetName("cWave");
    gWave = TH1F("aWave","test",1250000,0,1250000*1.6)
    gWave.SetName("aWave")
    for i in range(1250000):
        v = struct.unpack('h',bfile.read(2))
        #print i, v
        #gWave.SetPoint(i,1.6*i,v[0]*DimScale[0])
        gWave.SetBinContent(i+1,v[0]*DimScale[0]+DimOffset[0])
    #Curve Buffer - with variable length, contains all curve data in the specified format
    gWave.Draw("")
    gWave.GetXaxis().SetTitle("Time (ns)")
    gWave.GetYaxis().SetTitle("Voltage (V)")
    cCanvas.SaveAs(file_root)
    #WfmFileCheckSum - 8 bytes
    WfmFileCheckSum = struct.unpack('l',bfile.read(8))
    print "Wfm file check sum",WfmFileCheckSum[0]
