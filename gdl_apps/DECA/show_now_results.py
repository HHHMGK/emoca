import os, sys
from pathlib import Path

# import NoW related stuff
# sys.path += [str(Path(__file__).absolute().parents[3] / "now_evaluation")]
sys.path.insert(0, str(Path(__file__).absolute().parents[3] / "now_evaluation"))
from main import generating_cumulative_error_plots


def main():
    stage = 'detail'

    run_names = {}
    run_names['Original_DECA'] = "Paper DECA" # Original DECA from Yao
    # run_names['2021_03_18_21-10-25_DECA_training'] = "Basic DECA (trained by me)" # Basic DECA
    # run_names['2021_03_25_19-42-13_DECA_training'] = "My retrained with EmoNet loss" # DECA EmoNet
    # run_names['2021_03_29_23-14-42_DECA__EmoLossB_F2VAEw-0.00150_DeSegFalse_early'] = "Deca with EmoNetLoss" # DECA EmoNet
    # run_names['2021_03_26_15-05-56_DECA__DeSegFalse_DwC_early'] = "Detail with coarse jointly" # Detail with coarse
    # run_names['2021_03_26_14-36-03_DECA__DeSegFalse_DeNone_early'] = "DECA no detail exchange" # No detail exchange

    # aff-wild 2 models
    # run_names['2021_04_02_18-46-31_va_DeSegFalse_Aug_early'] = "AffWild DECA" # DECA
    # run_names['2021_04_02_18-46-47_va_EmoLossB_F2VAEw-0.00150_DeSegFalse_Aug_early'] = "AffWild with EmoNetLoss" # DECA with EmoNet
    # run_names['2021_04_02_18-46-34_va_DeSegFalse_Aug_DwC_early'] # DECA detail with coarse
    # run_names['2021_04_02_18-46-51_va_DeSegFalse_DeNone_Aug_DwC_early'] # DECA detail with coarse , no exchange


    # ### no-RING DECAs
    # # DECA dataset
    # run_names['2021_04_23_17-06-29_ExpDECA_DecaD_NoRing_EmoLossB_F2VAEw-0.00150_DeSegrend_DwC_early'] =\
    #     'DECA_DecaD_NoRing_EmoLossB_DwC'
    # run_names['2021_04_23_17-05-49_ExpDECA_DecaD_NoRing_EmoLossB_F2VAEw-0.00150_DeSegrend_early'] = \
    #     'DECA_DecaD_NoRing_EmoLossB'
    # run_names['2021_04_23_17-00-40_ExpDECA_DecaD_NoRing_DeSegrend_early'] = \
    #     'DECA_DecaD_NoRing'
    # # # run_names += ['']
    # #
    # # # # AffectNet
    # run_names['2021_04_23_17-12-20_DECA_Affec_NoRing_DeSegrend_DwC_early'] = \
    #     'DECA_Affec_NoRing_DwC'
    # run_names['2021_04_23_17-12-05_DECA_Affec_NoRing_DeSegrend_early'] = \
    #     'DECA_Affec_NoRing'
    # run_names['2021_04_23_17-11-08_DECA_Affec_NoRing_EmoLossB_F2VAEw-0.00150_DeSegrend_DwC_early'] = \
    #     'DECA_Affec_NoRing_EmoLossB_DwC'
    # run_names['2021_04_23_17-10-53_DECA_Affec_NoRing_EmoLossB_F2VAEw-0.00150_DeSegrend_early'] = \
    #     'DECA_Affec_NoRing_EmoLossB'

    run_names_new = {}
    # run_names_news += ['2021_06_23_21-03-02_DECA__EFswin_s_EFswin_s_DeSegFalse_early'] = "SWIN S"# DECA EmoNet
    run_names_new['2021_06_23_21-03-46_DECA__EFswin_t_EFswin_t_DeSegFalse_early'] = "SWIN T"
    run_names_new['2021_06_24_10-44-02_DECA__DeSegFalse_early'] = "DECA v1" # DECA EmoNets
    run_names_new['2021_08_29_00-38-20_DECA_DecaD_DeSegrend_Deex_early'] = "DECA v2" # DECA EmoNet
    run_names_new['2021_08_29_10-28-11_DECA_DecaD_VGGl_DeSegrend_Deex_early'] = "DECA with VGG loss"
    run_names_new['2021_08_29_10-31-15_DECAStar_DecaD_VGGl_DeSegrend_Deex_early'] = "DECA SWIN with VGG loss"
    run_names_new['2021_08_29_00-42-34_DECAStar_DecaD_DeSegrend_Deex_early'] = "DECAStar"
    run_names_new["2021_08_29_00-49-03_DECA_DecaD_EFswin_t_EDswin_t_DeSegrend_Deex_early"] = "DECA SWINT T"
    run_names_new["2021_08_29_00-48-58_DECAStar_DecaD_EFswin_t_EDswin_t_DeSegrend_Deex_early"] = "DECAStar SWINT T"
    run_names_new["2021_08_29_19-47-21_DECA_DecaD_EFswin_s_EDswin_s_VGGl_DeSegrend_Deex_early"] = "DECA SWIN-S + VGG loss"
    run_names_new["2021_08_29_19-47-28_DECAStar_DecaD_EFswin_s_EDswin_s_VGGl_DeSegrend_Deex_early"] = "DECAStar SWIN-S + VGG loss"



    use_dense_topology = False
    # use_dense_topology = True

    path_to_old_models = '/home/rdanecek/Workspace/mount/scratch/rdanecek/emoca/finetune_deca'
    path_to_new_models = '/is/cluster/work/rdanecek/emoca/finetune_deca'


    run_files = []
    nicks = []
    path_to_models = path_to_old_models
    for run_name, nick in run_names.items():
        if use_dense_topology:
            savefolder = Path(path_to_models) / run_name / stage / "NoW_dense"
        else:
            savefolder = Path(path_to_models) / run_name / stage / "NoW_flame"

        run_files += [str(savefolder / "results" / "_computed_distances.npy")]
        nicks += [nick]

    path_to_models = path_to_new_models
    for run_name, nick in run_names_new.items():
        if use_dense_topology:
            savefolder = Path(path_to_models) / run_name / stage / "NoW_dense"
        else:
            savefolder = Path(path_to_models) / run_name / stage / "NoW_flame"

        run_files += [str(savefolder / "results" / "_computed_distances.npy")]
        nicks += [nick]

    generating_cumulative_error_plots(run_files, nicks, "out.png")


if __name__ == "__main__":
    main()
