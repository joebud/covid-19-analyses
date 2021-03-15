# COVID-19 Analyses


CONTENTS


## COUNTRY ANALYSIS



### SCENARIO: no change in Rt
In this scenario, both the projected basic reproduction number and the projected 
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
- DEATHS
- FORECAST FIGURES




## EXTENDED ANALYSIS

### EARLY STAGES
 R0 SENSITIVITY


### AGE-AVERAGED PARAMETERS
### LOG GROWTH RATE
### CONTROL MEASURES
### SELF-OSCILLATIONS
### FORCED OSCILLATIONS
### SEASONAL FORCING
### LOCKDOWNS
### VACCINATIONS
### MINORS TESTING + VACCINATIONS
### REMOVAL DENSITIES
### INFECTION AGE
### WANING IMMUNITY
### MINIMUM PREVALENCE
### DETECTION PROBABILITY
### CONTACT TRACING
### VARIANTS
### VALIDITY



## COUNTRY COMPARISONS

## SCENARIO COMPARISONS


## BRIEF MODEL DESCRIPTION


### FEATURES

### MAIN ASSUMPTIONS

### DYNAMICS



### PARAMETERS

## KEY FINDINGS
NOT INCLUDED



## REFERENCES
NOT INCLUDED

## DOWNLOAD

COVID-19-ANALYSIS-{COUNTRY-CODE}-{TIME-SPAN}-{EXTENDED-ANALYSIS?}-{DATE}.pdf


