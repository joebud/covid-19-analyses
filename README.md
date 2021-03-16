# COVID-19 Analyses


CONTENTS


## COUNTRY ANALYSIS

- DATA AND PROJECTION PERIODS
- REFERENCE FRAME WRT INFECTION DATE
- UNCERTAINTY BANDS ON PLOTS OF TRUE CASES DENOTE MULTIPLICATIVE VARIATION OF R

- POPULATION
- NATURAL MORTALITY RATE
- INITIAL LOGARITHMIC GROWTH RATE 
- INITIAL INCIDENCE
- INITIALLY INFECTED POPULATION 
- APPROX. DATE OF FIRST INFECTION 
- INITIAL REPRODUCTION NUMBER (EXACT)
- INITIAL REPRODUCTION NUMBER (EXP. GROWTH)

- DURATION OF VIRAL SHEDDING
- AVG. CASE DURATION
- AVG. TIME TO RECOVERY
- AVG. TIME TO RECOVERY (MILD CASES)
- AVG. TIME TO RECOVERY (SEVERE CASES)
- AVG. TIME TO DEATH



### SCENARIO: no change in Rt
In this scenario, both the projected b    asic reproduction number and the projected 
effective mortality are assumed constant over the entire projection time period 
and are taken to be equal to the last observed values. No seasonality effects are 
taken into account. The effect of vaccinations is taken into account, 
the vaccination rate in the projection is taken to be zero, however.

### SCENARIO: seasonal changes
This scenario assumes seasonal variations in the basic reproduction number driven 
by variations in outdoor temperature and thus outdoor mobility. The maximum and 
minimum reproduction number is proportional to the corresponding values for 
seasonal influenza. The seasonal variations are then normalized such as to 
reproduce the initially observed, pre-lockdown reproduction number. The projection 
assumes the lockdown factor to remain constant, which is defined as the ratio 
of the seasonal reproduction number to the observed reproduction number. Again, 
the effect of vaccinations is taken into account based on historical data, 
the vaccination rate in the projection is taken to be zero, however.

### SCENARIO: seasonal + lockdowns
This scenario assumes exactly the same seasonal effects as in scenario 
\'seasonal changes\'. The effect of vaccinations is taken into account, 
the vaccination rate in the projection is taken to be zero, however. 
Lockdowns are modelled by multiplying the projected reproduction number 
by pulse functions with a quadratic rise and an exponential tail. The maximum 
lockdown factor is estimated from the previously observed data. A lockdown starts 
when the number of critical infections approaches the available capacity 
of the health care system (number of ICU beds) and ends when the number of 
all infections falls below a given percent of its initial value. The optimal 
threshold values have been found by minimizing the total lockdown duration over 
a long period of time. The projection does not assume a constant lockdown factor, 
as opposed to the previous scenarios, instead the projected lockdown factor 
relaxes after a pre-specified time period to a constant terminal value, 
which in general does not have to equal one (usually in the range 1 to 3). 
In lagged simulations, all pre-calculated lockdowns are shifted 
backwards in time by the specified time lag.

### SCENARIO: seasonal + vaccination
This scenario assumes exactly the same seasonal effects as in scenario 
\'seasonal changes\'. Vaccinations are accounted for using historical data 
and the vaccination rate (expressed as the fraction of population vaccinated 
per year) in the projection is set to a non-zero number, usually different 
from the currently observed vaccination rate. The projected lockdown factor 
relaxes after a pre-specified time period to a constant terminal value, 
which in general does not have to equal one (usually in the range 1 to 3). 
The susceptible population gets vaccinated in the first place. Vaccine-induced 
immunity wanes with a pre-specified age-specific rate, not necessarily equal 
to the duration of immunity after recovery from a natural infection.

### SCENARIO: seas. + vacc + variant (w/o imm.esc.)
This scenario is similar to scenario \'seasonal + vaccination\' with the only 
difference being the appearance of a new virus variant after a given time and 
with pre-specified multiplicative advantage (usually about 1.5). The projected 
lockdown factor relaxes after a pre-specified time period to a correspondingly 
lower terminal value as in scenarios without the variant. 

### SCENARIO: no control measures ever
This scenario assumes no control measures whatsoever (lockdowns, vaccinations, etc.) 
are ever taken. Seasonality effects are accounted for as in \'seasonal changes\'. 
Lockdown factor in the entire simulation is constant and equals one and 
no vaccinations take place. Mortality is assumed constant and is given by 
the effective mortality estimated from data.

### SCENARIO: influenza (novel, w/o measures)
This scenario assumes a novel hypothetical influenza-like virus with the same 
infection-age-specific characteristics and mortality as the seasonal influenza. 
Seasonality effects are accounted for similarly as in \'seasonal changes\', 
but with amplitudes scaled to reproduce those observed with seasonal influenza. 
Again, no control measures are even taken (no lockdowns, no vaccinations). 
Lockdown factor in the entire simulation is constant and equals one.


### FIGURES

- VACCINATED
- REPRODUCTION NUMBER
- MORTALITY
- INFECTED
- INFECTIOUS
- INCIDENCE
- TOTAL CASES
- RECOVERED
- SUSCEPTIBLE
- IMMUNE
- REINFECTIONS
- DEATH RATE
- DEATHS
- FORECAST FIGURES

- EFFECTIVELY VACCINATED
- INFECTED AND DEATHS FOR VARIOUS VACCINATION RATES 
- CRITICAL AND SEVERE INFECTIONS
- HOSPITAL AND ICU BEDS
- R SEASONAL
- LOCKDOWN FACTOR
- DEATH RATE DUE TO SEASONAL INFLUENZA
- AVG. DEATH RATE OVER LAST PROJECTION YEAR
- DEATHS INCL. CONTRIBUTION DUE TO NATURAL MORTALITY
- NATURAL DAILY DEATH RATE

- COMPARISON WITH SIMULATIONS USING A GIVEN SUBSET OF DATA ONLY


## EXTENDED ANALYSIS

### EARLY STAGES
- INITIAL LOGARITHMIC GROWTH RATE
- INITIAL INCIDENCE
- R0 SENSITIVITY

### AGE-AVERAGED PARAMETERS

- AGE-AVERAGED BETA, GAMMA, DELTA, AND R PARAMETERS

### LOG GROWTH RATE

- LOG GROWTH RATE
- MIN. ACHIEVABLE LAMBDA AT TIME T

### CONTROL MEASURES
- APPROX. TIME TO HALF I
- APPROX. TIME TO FLATTEN I 
- LOCKDOWN FACTOR
- LOCKDOWN FACTOR
- STRINGENCY INDEX
- SCHOOL CLOSING
- WORKSPACE CLOSING
- STAY-AT-HOME REQUIREMENTS
- FACIAL COVERINGS
- EFFECTIVENESS OF MEASURES
- FATIGUE FACTOR


### SELF-OSCILLATIONS
- IMPULSE RESPONSE
- STEP RESPONSE
- RAMP RESPONSE
- VARIOUS CONSTANT PROJECTION REPRODUCTION NUMBERS 
- VARIOUS NATURAL IMMUNITY DURATIONS (AT CONSTANT PROJECTION R)
- VARIOUS SCALES OF INFECTIOUSNESS DISTRIBUTION (AT CONSTANT PROJECTION R)
- LONG-TERM INFECTION PREVALENCE
- PHASE SPACE TRAJECTORIES
- AVG. FREQUENCY OF PEAKS IN INFECTION PREVALENCE
- AVG. FREQUENCY OF PEAKS ABOVE CAPACITY THRESHOLD
- LINEAR SPECTRUM (AT CONSTANT PROJECTION R)

### FORCED OSCILLATIONS

- VARIOUS FREQUENCIES OF FORCING (ABOUT A CONSTANT PROJECTION R)
- LONG-TERM INFECTION PREVALENCE
- PHASE SPACE TRAJECTORIES
- AVG. FREQUENCY OF PEAKS IN INFECTION PREVALENCE
- AVG. FREQUENCY OF PEAKS ABOVE CAPACITY THRESHOLD


### SEASONAL FORCING

- VARIOUS NATURAL IMMUNITY DURATIONS (WITH SAESONAL FORCING ON R)
- VARIOUS SCALES OF INFECTIOUSNESS DISTRIBUTION (WITH SAESONAL FORCING ON R)
- LONG-TERM RELAXATION OF LOCKDOWN FACTOR (BACK TO NORMAL)
- LONG-TERM INFECTION PREVALENCE
- PHASE SPACE TRAJECTORIES
- AVG. FREQUENCY OF PEAKS IN INFECTION PREVALENCE
- AVG. FREQUENCY OF PEAKS ABOVE CAPACITY THRESHOLD
- HYPOTHETICAL CASE OF PERSISTENT IMMUNITY
- CRITICAL AND SEVERE INFECTIONS
- HOSPITAL AND ICU BEDS

### LOCKDOWNS

- VARIOUS START/EXIT THRESHOLDS FOR LOCKDOWNS 
- LONG-TERM INFECTION PREVALENCE WITH LOCKDOWNS
- PHASE SPACE TRAJECTORIES
- AVG. FREQUENCY OF PEAKS IN INFECTION PREVALENCE
- AVG. FREQUENCY OF PEAKS ABOVE CAPACITY THRESHOLD
- LOCKDOWN START AND END DATES
- TOTAL LOCKDOWN DURATION AND COST 
- OPTIMAL THRESHOLDS
- CRITICAL AND SEVERE INFECTIONS
- HOSPITAL AND ICU BEDS

### VACCINATIONS

- VARIOUS PROJECTION VACCINATION RATES
- VARIOUS VACCINE-INDUCED IMMUNITY DURATIONS 
- VARIOUS NATURAL IMMUNITY DURATIONS 
- VARIOUS LONG-TERM LOCKDOWN RELAXATION FACTORS (NEW NORMAL)
- LONG-TERM INFECTION PREVALENCE WITH VACCINATIONS 
- VACCINE-INDUCED AND NATURAL IMMUNITIES
- EFFECTIVE REPRODUCTION NUMBER
- PHASE SPACE TRAJECTORIES
- AVG. FREQUENCY OF PEAKS IN INFECTION PREVALENCE
- AVG. FREQUENCY OF PEAKS ABOVE CAPACITY THRESHOLD
- TOTAL COST 
- HYPOTHETICAL CASE OF NO VACCINATIONS
- CRITICAL AND SEVERE INFECTIONS
- HOSPITAL AND ICU BEDS



### MINORS TESTING + VACCINATIONS

- EVERYDAY ANTIGEN TESTING OF MINORS 
- VARIOUS PROJECTION VACCINATION RATES
- LONG-TERM INFECTION PREVALENCE WITH VACCINATIONS AND MINORS' TESTING 
- VACCINE-INDUCED AND NATURAL IMMUNITIES
- EFFECTIVE REPRODUCTION NUMBER
- PHASE SPACE TRAJECTORIES
- AVG. FREQUENCY OF PEAKS IN INFECTION PREVALENCE
- AVG. FREQUENCY OF PEAKS ABOVE CAPACITY THRESHOLD
- TOTAL COST 
- HYPOTHETICAL CASE OF NO VACCINATIONS NOR TESTING
- CRITICAL AND SEVERE INFECTIONS
- HOSPITAL AND ICU BEDS
- CURRENT TESTING RATE AND POSITIVITY RATE


### REMOVAL DENSITIES

- REMOVAL DENSITIES DUE TO KERMACK VS. NOVEL REMOVAL DENSITIES 
- DIFFERENCES IN LONG-TERM INFECTION PREVALENCE AND MORTALITY


### INFECTION AGE

- AGELESS MODEL VS. INFECTION AGE MODEL (W/O WANING IMMUNITY AND VACCINATIONS)
- DIFFERENCES IN LONG-TERM INFECTION PREVALENCE AND MORTALITY
- COMPARISON WITH THEORETICAL LIMIT ON INFECTION PREVALENCE


### WANING IMMUNITY

- VARIOUS NATURAL IMMUNITY DURATIONS 
- COMPARISON WITH PERSISTENT IMMUNITY MODEL 
- DIFFERENCES IN LONG-TERM INFECTION PREVALENCE AND NUMBER OF REINFECTION CASES
- DECLINE IN RECOVERED AND IMMUNE FOR COMPARISON WITH EXPERIMENTAL STUDIES


### MINIMUM PREVALENCE

- LOWER LIMIT ON INFECTION PREVALENCE 
- COMPARISON WITH MODEL W/O LIMIT
- DIFFERENCES IN LONG-TERM INFECTION PREVALENCE AND NUMBER OF REINFECTION CASES
- DECLINE IN RECOVERED AND IMMUNE FOR COMPARISON WITH EXPERIMENTAL STUDIES


### DETECTION PROBABILITY

- VARIOUS PROBABILITIES OF DIAGNOSIS GIVEN SYMPTOMS
- DIFFERENCES IN LONG-TERM INFECTION PREVALENCE 


### CONTACT TRACING

- VARIOUS CUTOFFS ON INFECTIOUSNESS DISTRIBUTION 
- DIFFERENCES IN LONG-TERM INFECTION PREVALENCE 
- PERFECT CONTACT TRACING



### VARIANTS

- VARIOUS DATES OF FIRST APPEARANCE OF VARIANT (W/O IMMUNITY ESCAPE)
- FIXED MULTIPLICATIVE ADVANTAGE
- DIFFERENCES IN LONG-TERM INFECTION PREVALENCE FOR VARIANT AND ORIGINAL STRAIN 


### VALIDITY

- COMPARISON WITH THEORETICAL FINAL SIZE (FOR PERSISTENT IMMUNITY AND W/O VACCINATIONS)
- VARIOUS MODEL CHECKSUMS AND DISCREPANCY WITH OBSERVED DATA 


## COUNTRY COMPARISONS

### SCENARIOS

- COUNTRY COMPARISONS FOR EACH SCENARIO

### EARLY STAGES

- INITIAL LOGARITHMIC GROWTH RATE
- INITIAL INCIDENCE
- INITIAL REPRODUCTION NUMBER


## SCENARIO COMPARISONS

### CURRENT COUNTRY

- SCENARIO COMPARISONS FOR CURRENT COUNTRY

## BRIEF MODEL DESCRIPTION



### FEATURES


### MAIN ASSUMPTIONS


### DYNAMICS


### INITIAL CONDITIONS

### REPORTED VS TRUE CASES

### PARAMETER ESTIMATION

### AGE-SPECIFIC DISTRIBUTIONS

### VACCINATIONS

### TESTING

### SEASONALITY


### GLOSSARY


$^*$ - asterisk denotes ... , true otherwise

$t$ - Time since early stages of the epidemic

$\tau$   - age of infection (the time elapsed since the last infection)

$\tau'$ - Age of immunity (the time elapsed since the last recovery or vaccination)

$N$ - Total population


### PARAMETERS


## KEY FINDINGS



## REFERENCES



## DOWNLOAD

COVID-19-ANALYSIS-{COUNTRY-CODE}-{TIME-SPAN}-{EXTENDED-ANALYSIS?}-{DATE}.pdf





