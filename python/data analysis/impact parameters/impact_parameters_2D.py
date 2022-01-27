#====================================================
#     LIBRARIES AND SETTINGS
#====================================================
from ROOT import *
gROOT.SetBatch()
gROOT.LoadMacro( "AtlasStyle.C" )
gROOT.LoadMacro( "AtlasLabels.C" )

#====================================================
#     GLOBAL VARIABLES DECLARATION
#====================================================
lep_d0_pairs = [[],[]]
lep_z0_pairs = [[],[]]

#====================================================
#     PREPARING THE DATA
#====================================================
#Taking the .root file.
f = TFile ("rootfile_name.root")

#Extracting the Trees from the .root file.
t_reco = f.Get ("nominal")
t_truth = f.Get ("truth")

#Building an index for the truth tree, so it can be accessed as a friend of the reco tree.
t_truth.BuildIndex("eventNumber")
t_reco.AddFriend( t_truth )

#====================================================
#     CANVAS CREATION
#====================================================
c1 = TCanvas("c1", "d0significance and z0sintheta of e-mu leptons coming from tau or W (2 D)")
c1.Divide(2,2)

#====================================================
#     HISTOGRAMS CREATION
#====================================================
h_tau_d0significance_2D = TH2D ("h_tau_d0significance", "d_{0}significance for e-#mu coming from #tau in 2D", 100, -10, 10, 100, -4.5, 4.5)
h_tau_d0significance_2D.SetMarkerColor(kBlue)
h_tau_d0significance_2D.SetMinimum(0)
h_tau_d0significance_2D.GetXaxis().SetTitle("d_{0} for electrons")
h_tau_d0significance_2D.GetYaxis().SetTitle("d_{0} for muons")

h_tau_z0sintheta_2D = TH2D ("h_tau_z0sintheta", "z_{0}sin#theta for e-#mu coming from #tau in 2D", 100, -0.6, 0.6, 100, -0.6, 0.6)
h_tau_z0sintheta_2D.SetMarkerColor(kBlue)
h_tau_z0sintheta_2D.SetMinimum(0)
h_tau_z0sintheta_2D.GetXaxis().SetTitle("z_{0} sin #theta for electrons")
h_tau_z0sintheta_2D.GetYaxis().SetTitle("z_{0} sin #theta for muons")

h_W_d0significance_2D = TH2D ("h_W_d0significance", "d_{0}significance for e-#mu coming from W in 2D", 100, -8, 8, 100, -4.5, 4.5)
h_W_d0significance_2D.SetMarkerColor(kRed)
h_W_d0significance_2D.SetMinimum(0)
h_W_d0significance_2D.GetXaxis().SetTitle("d_{0} for electrons")
h_W_d0significance_2D.GetYaxis().SetTitle("d_{0} for muons")

h_W_z0sintheta_2D = TH2D ("h_W_z0sintheta", "z_{0}sin#theta for e-#mu coming from W in 2D", 100, -1, 1, 100, -1, 1)
h_W_z0sintheta_2D.SetMarkerColor(kRed)
h_W_z0sintheta_2D.SetMinimum(0)
h_W_z0sintheta_2D.GetXaxis().SetTitle("z_{0} sin #theta for electrons")
h_W_z0sintheta_2D.GetYaxis().SetTitle("z_{0} sin #theta for muons")

#====================================================
#     EVENT SELECTION AND HISTOGRAMS FILLING
#====================================================
for event in t_reco:

        #Reco level selection.
        if (event.passed_resolved_ejets_4j2b or event.passed_resolved_mujets_4j2b) and event.semileptonicEvent:

                #Defining some useful variables.
                weights = event.weight_mc * event.weight_pileup * event.weight_leptonSF * event.weight_bTagSF_DL1r_77 * event.weight_jvt

                #Truth level selection for electrons and muons coming from W.
                t_W1_electron = (abs(event.MC_Wdecay1_from_t_pdgId) == 11)
                t_W2_electron = (abs(event.MC_Wdecay2_from_t_pdgId) == 11)
                tbar_W1_electron = (abs(event.MC_Wdecay1_from_tbar_pdgId) == 11)
                tbar_W2_electron = (abs(event.MC_Wdecay2_from_tbar_pdgId) == 11)

                t_W1_muon = (abs(event.MC_Wdecay1_from_t_pdgId) == 13)
                t_W2_muon = (abs(event.MC_Wdecay2_from_t_pdgId) == 13)
                tbar_W1_muon = (abs(event.MC_Wdecay1_from_tbar_pdgId) == 13)
                tbar_W2_muon = (abs(event.MC_Wdecay2_from_tbar_pdgId) == 13)

                if t_W1_electron or t_W2_electron or tbar_W1_electron or tbar_W2_electron:
                        lep_d0_pairs[0] = []
                        lep_z0_pairs[0] = []
                        for i, j in zip(event.el_d0sig, event.el_delta_z0_sintheta):
                                lep_d0_pairs[0].append(i)
                                lep_z0_pairs[0].append(j)

                elif t_W1_muon or t_W2_muon or tbar_W1_muon or tbar_W2_muon:
                        lep_d0_pairs[1] = []
                        lep_z0_pairs[1] = []
                        for k, l in zip(event.mu_d0sig, event.mu_delta_z0_sintheta):
                                lep_d0_pairs[1].append(k)
                                lep_z0_pairs[1].append(l)

                if len(lep_d0_pairs[0]) != 0 and len(lep_d0_pairs[1]) != 0 and len(lep_z0_pairs[0]) != 0 and len(lep_z0_pairs[1]) != 0:
                        for x_1, x_2 in zip(lep_d0_pairs[0], lep_d0_pairs[1]):
                                h_W_d0significance_2D.Fill (x_1, x_2, weights)
                                lep_d0_pairs = [[],[]]
                        for y_1, y_2 in zip(lep_z0_pairs[0], lep_z0_pairs[1]):
                                h_W_z0sintheta_2D.Fill (y_1, y_2, weights)
                                lep_z0_pairs = [[],[]]

                #Truth level selection for electrons and muons coming from tau.
                t_W1_tau = (event.MC_Wdecay1_from_t_pdgId == 15)
                t_W1_antitau = (event.MC_Wdecay1_from_t_pdgId == -15)
                t_W2_tau = (event.MC_Wdecay2_from_t_pdgId == 15)
                t_W2_antitau = (event.MC_Wdecay2_from_t_pdgId == -15)

                tbar_W1_tau = (event.MC_Wdecay1_from_tbar_pdgId == 15)
                tbar_W1_antitau = (event.MC_Wdecay1_from_tbar_pdgId == -15)
                tbar_W2_tau = (event.MC_Wdecay2_from_tbar_pdgId == 15)
                tbar_W2_antitau = (event.MC_Wdecay2_from_tbar_pdgId == -15)

                lep_charge = event.el_charge[0] if len(event.el_charge) != 0 else event.mu_charge[0]

                t_W1_m = (event.MC_Wdecay1_from_t_m)
                t_W2_m = (event.MC_Wdecay2_from_t_m)
                tbar_W1_m = (event.MC_Wdecay1_from_tbar_m)
                tbar_W2_m = (event.MC_Wdecay2_from_tbar_m)

                if (t_W1_tau or t_W2_tau or tbar_W1_tau or tbar_W2_tau) and lep_charge < 0:
                        if event.passed_resolved_ejets_4j2b:
                                lep_d0_pairs[0] = []
                                lep_z0_pairs[0] = []
                                for m, n in zip(event.el_d0sig, event.el_delta_z0_sintheta):
                                        lep_d0_pairs[0].append(m)
                                        lep_z0_pairs[0].append(n)

                        elif event.passed_resolved_mujets_4j2b:
                                lep_d0_pairs[1] = []
                                lep_z0_pairs[1] = []
                                for o, p in zip(event.mu_d0sig, event.mu_delta_z0_sintheta):
                                        lep_d0_pairs[1].append(o)
                                        lep_z0_pairs[1].append(p)

                elif (t_W1_antitau or t_W2_antitau or tbar_W1_antitau or tbar_W2_antitau) and lep_charge > 0:
                        if event.passed_resolved_ejets_4j2b:
                                lep_d0_pairs[0] = []
                                lep_z0_pairs[0] = []
                                for m, n in zip(event.el_d0sig, event.el_delta_z0_sintheta):
                                        lep_d0_pairs[0].append(m)
                                        lep_z0_pairs[0].append(n)

                        elif event.passed_resolved_mujets_4j2b:
                                lep_d0_pairs[1] = []
                                lep_z0_pairs[1] = []
                                for o, p in zip(event.mu_d0sig, event.mu_delta_z0_sintheta):
                                        lep_d0_pairs[1].append(o)
                                        lep_z0_pairs[1].append(p)

                if len(lep_d0_pairs[0]) != 0 and len(lep_d0_pairs[1]) != 0 and len(lep_z0_pairs[0]) != 0 and len(lep_z0_pairs[1]) != 0:
                        for z_1, z_2 in zip(lep_d0_pairs[0], lep_d0_pairs[1]):
                                h_tau_d0significance_2D.Fill (z_1, z_2, weights)
                                lep_d0_pairs = [[],[]]
                        for t_1, t_2 in zip(lep_z0_pairs[0], lep_z0_pairs[1]):
                                h_tau_z0sintheta_2D.Fill (t_1, t_2, weights)
                                lep_z0_pairs = [[],[]]

#====================================================
#     SAVING HISTOGRAMS
#====================================================
gStyle.SetPalette(1)
c1.cd(1)
gPad.SetLogz()
ATLASLabel( 0.65, 0.8, "Internal" )
h_tau_d0significance_2D.Draw("COLZ")
c1.cd(2)
gPad.SetLogz()
ATLASLabel( 0.65, 0.8, "Internal" )
h_tau_z0sintheta_2D.Draw("COLZ")
c1.cd(3)
gPad.SetLogz()
ATLASLabel( 0.65, 0.8, "Internal" )
h_W_d0significance_2D.Draw("COLZ")
c1.cd(4)
gPad.SetLogz()
ATLASLabel( 0.65, 0.8, "Internal" )
h_W_z0sintheta_2D.Draw("COLZ")

#Saving canvas.
c1.Print( "d0_z0_canvas_2D.root")

#Saving histograms.
f_out = TFile ("impact_parameters_histograms_2D.root", "recreate")
h_tau_d0significance_2D.SetDirectory(f_out)
h_tau_z0sintheta_2D.SetDirectory(f_out)
h_W_d0significance_2D.SetDirectory(f_out)
h_W_z0sintheta_2D.SetDirectory(f_out)
f_out.Write()
f_out.Close()

