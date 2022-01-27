#====================================================
#     LIBRARIES AND SETTINGS
#====================================================
from ROOT import *
gROOT.SetBatch()
gROOT.LoadMacro( "AtlasStyle.C" )
gROOT.LoadMacro( "AtlasLabels.C" )
SetAtlasStyle()

#====================================================
#     FUNCTION TO MAKE CANVAS
#====================================================
def MakeCanvas( split = 0.25 ):
    c = TCanvas( "DataPrediction", "Data/Prediction", 800, 800 )
    pad0 = TPad("pad0","pad0", 0.0, 0.273, 1.0, 1.00)
    pad1 = TPad("pad1","pad1", 0.0, 0.008, 1.0, 0.272)
    pad0.SetBottomMargin(0.001)
    pad0.SetBorderMode(0)
    pad1.SetBottomMargin(0.45)
    pad0.SetTicks(1,1)
    pad1.SetTicks(1,1)
    pad0.Draw()
    pad1.Draw()
    pad0.cd()
    return c, pad0, pad1

def main():
    #====================================================
    #     PREPARING THE DATA
    #====================================================
    
    #Taking the .root file.
    f = TFile ("rootfile_name.root")
    
    #Extracting the histograms from the .root file.
    variables = [ "d0significance", "z0sintheta" ]
    titles = [ "d_0", "z_0 sin #theta" ]
    leptons = [ "", "_e", "_mu" ]
    
    #Creating the Canvas.
    c, pad0, pad1 = MakeCanvas()
    pad0.SetLogy()
    
    #====================================================
    #     SAVING HISTOGRAMS
    #====================================================
    f_out = TFile ("comparison_histograms.root", "recreate")
    ratios = []
    for variable in variables:
        if variable == "d0significance":
                title = "d_{0}"
        else:
             	title = "z_{0} sin #theta"
        for lepton in leptons:
            hname_tau = "h_tau_" + variable + lepton
            hname_W = "h_W_" + variable + lepton
            h_tau = f.Get( hname_tau )
            h_tau.Rebin(4)
            h_tau.Scale( 1. / h_tau.Integral() )
            h_tau.SetLineColor( kRed )
            h_tau.SetMarkerColor( kRed )
            h_tau.SetTitle( "leptons from #tau " )
            h_tau.GetXaxis().SetTitle( title )
            h_tau.GetXaxis().SetTitleSize(.15)
            h_tau.GetYaxis().SetTitle( "Events" )
            h_tau.GetYaxis().SetLabelSize(.040)
            h_W = f.Get( hname_W )
            h_W.Rebin(4)
            h_W.Scale( 1. / h_W.Integral() )
            h_W.GetXaxis().SetTitle( title )
            h_W.GetYaxis().SetTitle( "Events" )
            h_W.SetTitle( "leptons from W" )
            h_W.GetYaxis().SetLabelSize(.040)
            h_ratio = h_tau.Clone()
            h_ratio.GetYaxis().SetTitle( "#tau / W" )
            h_ratio.GetYaxis().SetTitleSize(.15)
            h_ratio.GetYaxis().SetTitleOffset(.48)
            h_ratio.GetYaxis().SetLabelSize(.1)
            h_ratio.GetYaxis().SetLabelOffset(.03)
            h_ratio.GetYaxis().SetNdivisions(5)
            h_ratio.GetXaxis().SetLabelSize(.10)
            h_ratio.GetXaxis().SetLabelOffset(.07)
            h_ratio.Divide( h_W )
            h_ratio.SetDirectory( f_out )
            pad0.cd()
            h_W.Draw( "hist" )
            h_tau.Draw( "hist same" )
            
            #TLegend settings:
            leg = TLegend(0.17,0.7,0.48,0.9)
            leg.SetFillColor(0)
            leg.SetFillStyle(0)
            leg.SetLineColor(0)
            leg.SetBorderSize(0)
            leg.SetTextFont(42)
            leg.SetTextSize(0.04)
            leg.AddEntry(h_W,"Leptons from W")
            leg.AddEntry(h_tau,"Leptons from #tau")
            leg.Draw()
            ATLASLabel( 0.65, 0.8, "Internal" )
            pad1.cd()
            h_ratio.Draw( "" )
            ratios.append( h_ratio )
            c.Print( variable + lepton + ".pdf" )
            c.Print( variable + lepton + ".root" )

    f_out.Write()
    f_out.Close()

if __name__ == "__main__":
        main()
