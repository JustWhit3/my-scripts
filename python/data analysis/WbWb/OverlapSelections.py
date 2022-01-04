#!/usr/bin/env python


##############################    Import libraries    ##############################


import os, sys
import optparse
from distutils.dir_util import mkpath
import numpy as np

from ROOT import *
sys.path.append('../../utils/')
import helper_functions

gROOT.SetMacroPath('../../utils/')
gROOT.Macro( "rootlogon.C" )
gROOT.LoadMacro( "AtlasUtils.C" )

gROOT.SetBatch(True)


##############################    Function to make ATLAS label in a plot    ##############################


def MakeATLASLabel( x, y, status = "Internal", iLumi = "139", ECM = "13" ):
    ATLAS_LABEL( x, y, kBlack )

    myText( x+0.16, y, kBlack, status )

    text  = "#sqrt{s} = %s TeV, %s fb^{-1}" % ( ECM, iLumi )

    l = TLatex()
    l.SetTextSize(0.035); 
    l.SetNDC()
    l.SetTextColor(kBlack)
    l.DrawLatex( x, y-0.05, text)


##############################    Main code    ##############################


if __name__ == "__main__":
   
   #Main options
   parser = optparse.OptionParser( usage = "%prog [options] configfile.xml" )
   parser.add_option( "-b", "--batch", help="Batch mode [%default]", dest="batch", default=True )

   (opts, args) = parser.parse_args()
 
   if opts.batch:
        gROOT.SetBatch(True)
        
   #Create path to save modified histograms
   exts =  ["png", "pdf" ]
   for ext in exts:
      mkpath( "./img/" + ext + "/selections" ) 

   #Variables and TCanvas declarations and inizializations
   standard_path = "../../scripts_WbWb_dilepton_fullrun2/results/" 
   histogram = {}
   lparams = { 'xoffset' : 0.17, 'yoffset' : 0.38, 'width'   : 0.80, 'height'  : 0.04 }
   colors = [ kOrange, kSpring, kBlue, kBlack, kRed, kCyan-3, kMagenta+2, kOrange+3, kGreen+3 ]

   xsecs = [ "AbsoluteDiffXs", "RelativeDiffXs" ]
   
   selections = [ "2j2b60_0extrab70_emu", "2j2b60_0extrab77_emu", "2j2b60_0extrab85_emu", "2j2b70_0extrab77_emu",  
                  "2j2b70_0extrab85_emu", "2j2b77_0extrab85_emu", "2jexcl2b60_emu", "2jexcl2b70_emu" ]
                  
   variables = [ "minimaxmbl", "DR_b1b2" ]
          
   #This list should have 1:1 correspondance to the "variable" list     
   variables_title = [ "m^{minimax}_{bl} [GeV]", "#Delta R^{b1b2}" ]
   
   # "#Delta #phi^{l1l2}", "m^{l1l2} [GeV]"
   
   groups = [ "statsyst", "statonly", "group_jes", "group_btagging", "group_lepton", "group_backgrounds", "group_ifsr", "group_pileup", "group_lumi", "group_tW_modelling", "group_ttbar_modelling", "group_PS", "group_generator" ]

   #This list should have 1:1 correspondance to the "variable" list
   groups_label = [ "Stat.+Syst. Unc.", "Stat. Unc.", "JES/JER", "Flavour Tagging", "Leptons", "Backgrounds", "MC Stat.", "Pileup", "Luminosity", "tW modelling", "ttbar modelling", "PS", "Generators" ]
   
   #Canvas creation
   c = TCanvas( "c", "c", 800, 800 )
   gPad.SetLeftMargin( 0.16 )
   gPad.SetRightMargin( 0.05 )
   gPad.SetBottomMargin( 0.15 )
   gPad.SetTopMargin( 0.02 )

   #Start of the histogram processing
   for xsec in xsecs:
      for variable, variable_title in zip( variables, variables_title ):
         for group, group_label in zip( groups, groups_label ):
         
            counter = 0
            
            #Legend creation
            leg = helper_functions.MakeLegend( lparams )
            leg.SetTextFont( 42)
            leg.SetNColumns(2)
            leg.SetTextSize(0.026)
            leg.SetTextAlign(11)
            
            for selection, color in zip( selections, colors ):
            
               infile = TFile.Open( standard_path + selection + "/WbWb_dilepton_" + selection + "_" + 
                                    variable + ".fractional_uncertainties." + xsec + ".root" )
     
               for var in [ 'u', 'd' ]:
                  histogram[ selection + "_" + var ] = infile.Get( group + "_" + var ).Clone()
                  histogram[ selection + "_" + var ].SetDirectory(0)
        
                  if counter == 0:
                     #Basic histogram style settings
                     histogram[ selection + "_" + var ].SetMaximum(  50 )
                     histogram[ selection + "_" + var ].SetMinimum( -50 )  
                     histogram[ selection + "_" + var ].GetYaxis().SetTitle( "Fractional Uncertainty [%]" )
                     histogram[ selection + "_" + var ].GetYaxis().SetLabelSize( 0.04 )
                     histogram[ selection + "_" + var ].GetXaxis().SetTitleSize( 0.04 )
                     histogram[ selection + "_" + var ].GetXaxis().SetLabelSize( 0.04 )
                     histogram[ selection + "_" + var ].GetXaxis().SetTitle( variable_title )
                     #histogram[ selection + "_" + var ].SetTitle( group )
                     histogram[ selection + "_" + var ].SetLineColor( color )
                     histogram[ selection + "_" + var ].SetLineStyle(1)
                     histogram[ selection + "_" + var ].SetLineWidth(2)
                     histogram[ selection + "_" + var ].Draw()
                     
                  else:
                     #Basic histogram style settings
                     histogram[ selection + "_" + var ].SetLineColor( color )
                     histogram[ selection + "_" + var ].SetLineStyle(1)
                     histogram[ selection + "_" + var ].SetLineWidth(2)
                     histogram[ selection + "_" + var ].Draw("same")
                     
                  counter += 1
                     
               #Other histogram and legend settings                 
               leg.AddEntry( histogram[ selection + "_" + var ], selection, "l" )
                   
               MakeATLASLabel( 0.18, 0.90, "Internal", "139", "13" )
               text1 = TLatex()
               text1.SetNDC()
               text1.SetTextSize(0.035)
               text1.DrawText(  0.18, 0.80, "WbWb dilepton" )    
               text1.DrawText(  0.58, 0.90, "Fiducial phase-space" )
               if xsec == "AbsoluteDiffXs":
                  text1.DrawText(  0.58, 0.85, "Absolute cross-section" )    
               else:
                  text1.DrawText(  0.58, 0.85, "Normalised cross-section" )
               text1.DrawText(  0.58, 0.80, group_label )
                     
            #Draw legends
            leg.Draw()
            leg.SetY1( leg.GetY1() - lparams["height"] * leg.GetNRows() )
       
            #Writing histograms in the Canvas and saving this latter         
            plotname = "WbWb_dilepton_" + variable + "." + group + "." + xsec
            gPad.RedrawAxis()
            c.cd()
            for ext in exts:
               img = "img/%s/selections/%s.%s" % ( ext, plotname, ext )
               c.SaveAs( img ) 
  


   