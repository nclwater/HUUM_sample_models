import huum_model.huum as huum

def run_model(input_name: str, fn_config: str):

    print(
        '\n--------------------------------------------------------------------------------'
    )
    print(f'\nDoing Testrun for {input_name}...')

    print('\n   Loading data...')
    model = huum.HUUM()
    model.load(fn_config)

    print('\n   ...running model...')

    model.run()

    print('\n   ...finished.\n')


# 3. Main Exec =================================================================
if __name__ == '__main__':

    # run_model('Lifecycle Dev', 'development/lifecycle.yaml')
    run_model('Shower with Leakage Dev', 'development/shower_leakage.yaml')
    run_model('Complete Household Dev', 'development/complete_household.yaml')
    
    run_model('Baseline Model: Long Peak', 'baseline/long_peak.yaml')
    run_model('Baseline Model: Evening Peak', 'baseline/one_peak_evening_peak.yaml')
    run_model('Baseline Model: Morning Peak', 'baseline/one_peak_morning_peak.yaml')
    run_model('Baseline Model: Two Peaks', 'baseline/two_peaks.yaml')