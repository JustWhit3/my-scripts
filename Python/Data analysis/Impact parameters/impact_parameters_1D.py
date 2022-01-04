#====================================================
#     LIBRARIES AND SETTINGS
#====================================================
from ROOT import *
gROOT.SetBatch()

#====================================================
#     PREPARING THE DATA
#====================================================
#Taking the .root file.
f = TFile ("user.mromano.21119792._000057.ljets.output.root")

#Extracting the Trees from the .root file.
t_reco = f.Get ("nominal")
t_truth = f.Get ("truth")

#Building an index for the truth tree, so it can be accessed as a friend of the reco tree.
t_truth.BuildIndex("eventNumber")
t_reco.AddFriend( t_truth )

#====================================================
#     CANVAS CREATION
#====================================================
c1 = TCanvas("c1", "d0significance and z0sintheta of leptons coming from tau or W (1 D)")
c1.Divide(2,2)

c2 = TCanvas("c2", "d0significance and z0sintheta of e coming from tau or W (1 D)")
c2.Divide(2,2)

c3 = TCanvas("c3", "d0significance and z0sintheta of #mu coming from tau or W (1 D)")
c3.Divide(2,2)

#====================================================
#     HISTOGRAMS CREATION
#====================================================
h_tau_d0significance = TH1F ("h_tau_d0significance", "d_{0}significance for leptons coming from #tau", 100, -6, 6)
h_tau_d0significance.SetLineColor(kBlue)
h_tau_d0significance_e = TH1F ("h_tau_d0significance_e", "d_{0}significance for e coming from #tau", 100, -6, 6)
h_tau_d0significance_e.SetLineColor(kBlue)
h_tau_d0significance_mu = TH1F ("h_tau_d0significance_mu", "d_{0}significance for #mu coming from #tau", 100, -6, 6)
h_tau_d0significance_mu.SetLineColor(kBlue)

h_tau_z0sintheta = TH1F ("h_tau_z0sintheta", "z_{0}sin#theta for leptons coming from #tau", 100, -0.6, 0.6)
h_tau_z0sintheta.SetLineColor(kBlue)
h_tau_z0sintheta_e = TH1F ("h_tau_z0sintheta_e", "z_{0}sin#theta for e coming from #tau", 100, -0.6, 0.6)
h_tau_z0sintheta_e.SetLineColor(kBlue)
h_tau_z0sintheta_mu = TH1F ("h_tau_z0sintheta_mu", "z_{0}sin#theta for #mu coming from #tau", 100, -0.6, 0.6)
h_tau_z0sintheta_mu.SetLineColor(kBlue)

h_W_d0significance = TH1F ("h_W_d0significance", "d_{0}significance for leptons coming from W", 100, -6, 6)
h_W_d0significance.SetLineColor(kRed)
h_W_d0significance_e = TH1F ("h_W_d0significance_e", "d_{0}significance for e coming from W", 100, -6, 6)
h_W_d0significance_e.SetLineColor(kRed)
h_W_d0significance_mu = TH1F ("h_W_d0significance_mu", "d_{0}significance for #mu coming from W", 100, -6, 6)
h_W_d0significance_mu.SetLineColor(kRed)

h_W_z0sintheta = TH1F ("h_W_z0sintheta", "z_{0}sin#theta for leptons coming from W", 100, -0.6, 0.6)
h_W_z0sintheta.SetLineColor(kRed)
h_W_z0sintheta_e = TH1F ("h_W_z0sintheta_e", "z_{0}sin#theta for e coming from W", 100, -0.6, 0.6)
h_W_z0sintheta_e.SetLineColor(kRed)
h_W_z0sintheta_mu = TH1F ("h_W_z0sintheta_mu", "z_{0}sin#theta for #mu coming from W", 100, -0.6, 0.6)
h_W_z0sintheta_mu.SetLineColor(kRed)

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
                        for i, j in zip(event.el_d0sig, event.el_delta_z0_sintheta):
                                h_W_d0significance.Fill (i, weights)
                                h_W_z0sintheta.Fill (j, weights)
                                h_W_d0significance_e.Fill (i, weights)
                                h_W_z0sintheta_e.Fill (j, weights)

                if t_W1_muon or t_W2_muon or tbar_W1_muon or tbar_W2_muon:
                        for k, l in zip(event.mu_d0sig, event.mu_delta_z0_sintheta):
                                h_W_d0significance.Fill (k, weights)
                                h_W_z0sintheta.Fill (l, weights)
                                h_W_d0significance_mu.Fill (k, weights)
                                h_W_z0sintheta_mu.Fill (l, weights)

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

                if (t_W1_tau or t_W2_tau or tbar_W1_tau or tbar_W2_tau) and lep_charge < 0:
                        if event.passed_resolved_ejets_4j2b:
                                for m, n in zip(event.el_d0sig, event.el_delta_z0_sintheta):
                                        h_tau_d0significance.Fill (m, weights)
                                        h_tau_z0sintheta.Fill (n, weights)
                                        h_tau_d0significance_e.Fill (m, weights)
                                        h_tau_z0sintheta_e.Fill (n, weights)

                        elif event.passed_resolved_mujets_4j2b:
                                for o, p in zip(event.mu_d0sig, event.mu_delta_z0_sintheta):
                                        h_tau_d0significance.Fill (o, weights)
                                        h_tau_z0sintheta.Fill (p, weights)
                                        h_tau_d0significance_mu.Fill (o, weights)
                                        h_tau_z0sintheta_mu.Fill (p, weights)

                elif (t_W1_antitau or t_W2_antitau or tbar_W1_antitau or tbar_W2_antitau) and lep_charge > 0:
                        if event.passed_resolved_ejets_4j2b:
                                for m, n in zip(event.el_d0sig, event.el_delta_z0_sintheta):
                                        h_tau_d0significance.Fill (m, weights)
                                        h_tau_z0sintheta.Fill (n, weights)
                                        h_tau_d0significance_e.Fill (m, weights)
                                        h_tau_z0sintheta_e.Fill (n, weights)

                        elif event.passed_resolved_mujets_4j2b:
                                for o, p in zip(event.mu_d0sig, event.mu_delta_z0_sintheta):
                                        h_tau_d0significance.Fill (o, weights)
                                        h_tau_z0sintheta.Fill (p, weights)
                                        h_tau_d0significance_mu.Fill (o, weights)
                                        h_tau_z0sintheta_mu.Fill (p, weights)

#====================================================
#     SAVING HISTOGRAMS
#====================================================
gStyle.SetPalette(1)

c1.cd(1)
h_tau_d0significance.Draw()
c1.cd(2)
h_tau_z0sintheta.Draw()
c1.cd(3)
h_W_d0significance.Draw()
c1.cd(4)
h_W_z0sintheta.Draw()

c2.cd(1)
h_tau_d0significance_e.Draw()
c2.cd(2)
h_tau_z0sintheta_e.Draw()
c2.cd(3)
h_W_d0significance_e.Draw()
c2.cd(4)
h_W_z0sintheta_e.Draw()

c3.cd(1)
h_tau_d0significance_mu.Draw()
c3.cd(2)
h_tau_z0sintheta_mu.Draw()
c3.cd(3)
h_W_d0significance_mu.Draw()
c3.cd(4)
h_W_z0sintheta_mu.Draw()

#Saving canvas.
c1.Print( "d0_z0_canvas.root")
c2.Print( "d0_z0_canvas_e.root")
c3.Print( "d0_z0_canvas_mu.root")

#Saving histograms.
f_out = TFile ("impact_parameters_histograms.root", "recreate")
h_tau_d0significance.SetDirectory(f_out)
h_tau_z0sintheta.SetDirectory(f_out)
h_W_d0significance.SetDirectory(f_out)
h_W_z0sintheta.SetDirectory(f_out)

h_tau_d0significance_e.SetDirectory(f_out)
h_tau_z0sintheta_e.SetDirectory(f_out)
h_W_d0significance_e.SetDirectory(f_out)
h_W_z0sintheta_e.SetDirectory(f_out)

h_tau_d0significance_mu.SetDirectory(f_out)
h_tau_z0sintheta_mu.SetDirectory(f_out)
h_W_d0significance_mu.SetDirectory(f_out)
h_W_z0sintheta_mu.SetDirectory(f_out)

f_out.Write()
f_out.Close()

