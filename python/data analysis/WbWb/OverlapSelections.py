#!/usr/bin/env python

#############################################################
#    Import libraries
#############################################################
import os, sys
import argparse
from distutils.dir_util import mkpath
import numpy as np
from ROOT import *
sys.path.append('../../utils/')
import helper_functions

#############################################################
#    Global settings
#############################################################
gROOT.SetMacroPath('../../utils/')
gROOT.Macro( "rootlogon.C" )
gROOT.LoadMacro( "AtlasUtils.C" )
gROOT.SetBatch(True)

#############################################################
#    "MakeATLASLabel" function
#############################################################
def MakeATLASLabel( x, y, status = "Internal", iLumi = "139", ECM = "13" ):
   """
   Function to make the ATLAS label.

   Args:
       x (float): x-coordinate position of the label.
       y (float): y-coordinate position of the label.
       status (str, optional): Status of the plot. Defaults to "Internal".
       iLumi (str, optional): Luminosity value. Defaults to "139".
       ECM (str, optional): Center-of-mass energy. Defaults to "13".
   """
   
   ATLAS_LABEL( x, y, kBlack )
   myText( x+0.16, y, kBlack, status )
   text  = "#sqrt{s} = %s TeV, %s fb^{-1}" % ( ECM, iLumi )
   l = TLatex()
   l.SetTextSize(0.035); 
   l.SetNDC()
   l.SetTextColor(kBlack)
   l.DrawLatex( x, y-0.05, text)
    
#############################################################
#    "initialize_basic" function
#############################################################
def initialize_basic( args ):
   """
   Function used to initialize basic plot settings.

   Returns:
       any: Returns basic plot settings: exts, standard_path, histogram, lparams, colors.
   """
   
   exts =  [ "png", "pdf" ]
   for ext in exts:
      mkpath( "./img/" + ext + "/selections" ) 

   histogram = {}
   histogram_old = {}
   standard_path = "../../scripts_WbWb_dilepton_fullrun2/results/"
   standard_path_old = "../../scripts_WbWb_dilepton_fullrun2/results_backup/"  
   lparams = { 'xoffset' : 0.17, 'yoffset' : 0.38, 'width'   : 0.80, 'height'  : 0.04 }
   
   if args.old:
      colors = [ kBlue ]
   else:
      colors = [ kOrange, kSpring, kBlue, kBlack, kRed, kCyan-3, kMagenta+2, kOrange+3, kGreen+3 ]
   
   return exts, standard_path, standard_path_old, histogram, histogram_old, lparams, colors

#############################################################
#    "initialize_vars" function
#############################################################
def initialize_vars( args ):
   """
   Function used to return variables initialization.

   Returns:
       any: Returns variables values: xsecs, selections, variables, variables_title, groups, c.
   """

   xsecs = [
      "AbsoluteDiffXs", 
      "RelativeDiffXs" 
      ]
   
   if args.old: 
      selections = [
         args.old, 
         "2jexcl2b60_emu" 
         ]
      variables = {
         "minimaxmbl_old": "m^{minimax}_{bl} old [GeV]" 
         }
   else:
      selections = [
         "2j2b60_0extrab70_emu", 
         "2j2b60_0extrab77_emu", 
         "2j2b60_0extrab85_emu", 
         "2j2b70_0extrab77_emu",  
         "2j2b70_0extrab85_emu", 
         "2j2b77_0extrab85_emu", 
         "2jexcl2b60_emu", 
         "2jexcl2b70_emu" 
         ]         
      variables = {
         "minimaxmbl": "m^{minimax}_{bl} [GeV]", 
         "DR_b1b2": "#Delta R^{b1b2}" 
         }

   groups = {
      "statsyst": "Stat.+Syst. Unc.", 
      "statonly": "Stat. Unc.", 
      "group_jes": "JES/JER", 
      "group_btagging": "Flavour Tagging", 
      "group_lepton": "Leptons", 
      "group_backgrounds": "Backgrounds", 
      "group_ifsr": "MC Stat.", 
      "group_pileup": "Pileup", 
      "group_lumi": "Luminosity", 
      "group_tW_modelling": "tW modelling", 
      "group_ttbar_modelling": "ttbar modelling", 
      "group_PS": "PS", 
      "group_generator": "Generators",  
      }

   c = TCanvas( "c", "c", 800, 800 )
   gPad.SetLeftMargin( 0.16 )
   gPad.SetRightMargin( 0.05 )
   gPad.SetBottomMargin( 0.15 )
   gPad.SetTopMargin( 0.02 )
   
   return xsecs, selections, variables, groups, c

#############################################################
#    "plotter_settings" function
#############################################################
def plotter_settings( infile, histogram, selection, var, group, counter, variable_title, color ):
   """
   Function to set-up all the plot settings.

   Args:
       args(parse): parsed commands.
       histogram (list): list of the needed histograms.
       selection (str): b-tagging selection.
       var (str): up or down flavour of the variable.
       group (str): systematic name.
       counter (int): the counter used for the loops.
       variable_title (str): variable title.
       color (TColor): histogram line color.
       
      
   returns: returns the modified histogram and the increased counter.
   """
   
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
   
   return histogram[ selection + "_" + var ], counter

#############################################################
#    "plotter_settings_old" function
#############################################################
def plotter_settings_old( infile, histogram_old, selection, var, group ):
   """
   Function to set-up all the plot settings.

   Args:
       args(parse): parsed commands.
       histogram (list): list of the needed histograms.
       selection (str): b-tagging selection.
       var (str): up or down flavour of the variable.
       group (str): systematic name.
       counter (int): the counter used for the loops.
       variable_title (str): variable title.
       
   returns: returns the modified histogram and the increased counter.
   """
   
   histogram_old[ selection + "_" + var ] = infile.Get( group + "_" + var ).Clone()
   histogram_old[ selection + "_" + var ].SetDirectory(0)
      
   #Basic histogram style settings
   histogram_old[ selection + "_" + var ].SetLineColor( kRed )
   histogram_old[ selection + "_" + var ].SetLineStyle(1)
   histogram_old[ selection + "_" + var ].SetLineWidth(2)
   histogram_old[ selection + "_" + var ].Draw("same")
      
   return histogram_old[ selection + "_" + var ]

#############################################################
#    "plotter" function
#############################################################
def plotter( args, exts, standard_path, standard_path_old, histogram, histogram_old, lparams, colors, xsecs, selections, variables, groups, c ):
   """
   Function used to select events and plot result.

   Args:
       exts (list): contains extension information.
       standard_path (str): standard path for input file.
       histogram (dict): empty dict used later for analysis.
       lparams (dict): used for TLegend parameters.
       colors (list): contains the color list.
       xsecs (list): list of cross-sections type.
       selections (list): list of selections types.
       variables (list): list of variable types.
       variables_title (list): list of variable titles.
       groups (list): list of groups types.
       groups_label (list): list of groups labels.
       c (TCanvas): final Canvas for plots.
   """     
      
   #Starting the real function part:
   for xsec in xsecs:
      for variable, variable_title in variables.items():
         for group, group_label in groups.items():
         
            counter = 0
            
            #Legend creation
            leg = helper_functions.MakeLegend( lparams )
            leg.SetTextFont( 42)
            if args.old:
               leg.SetNColumns(1)
            else:
               leg.SetNColumns(2)
            leg.SetTextSize(0.026)
            leg.SetTextAlign(11)
            
            #Applying selections and plot features using previously defined functions
            for selection, color in zip( selections, colors ):
               infile = TFile.Open( standard_path + selection + "/WbWb_dilepton_" + selection + "_" + variable + ".fractional_uncertainties." + xsec + ".root" )
               
               if args.old:
                  infile_2 = TFile.Open( standard_path_old + selection + "/WbWb_dilepton_" + selection + "_" + variable + ".fractional_uncertainties." + xsec + ".root" )
     
               for var in [ 'u', 'd' ]:
                  histogram[ selection + "_" + var ], counter = plotter_settings( infile, histogram, selection, var, group, counter, variable_title, color )
                  
                  if args.old:
                     histogram_old[ selection + "_" + var ] = plotter_settings_old( infile_2, histogram_old, selection, var, group )

               #Other histogram and legend settings      
               if args.old:
                  new_ = args.old + " (w/ tt + HF)"
                  old_ = args.old
                  #PUT A CONDITION HERE FOR THE 2JEXC LINE
                  leg.AddEntry( histogram[ selection + "_" + var ], new_, "l" )
                  leg.AddEntry( histogram_old[ selection + "_" + var ], old_, "l" )
               else:
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

#############################################################
#    Main function
#############################################################
def main():
   parser = argparse.ArgumentParser( description = "Produces selection plots." )
   parser.add_argument( "-o", "--old", help = "Produces plots with tt+HF uncertainty from the old measurement" )
   args = parser.parse_args()
   
   exts, standard_path, standard_path_old, histogram, histogram_old, lparams, colors = initialize_basic( args )
   xsecs, selections, variables, groups, c = initialize_vars( args )
   
   plotter( args, exts, standard_path, standard_path_old, histogram, histogram_old, lparams, colors, xsecs, selections, variables, groups, c )
        
if __name__ == "__main__":
   main()