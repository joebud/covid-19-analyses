 
# COVID-19 Projections

Generating COVID-19 projections for various scenarios and countries

[//]: # CONTENTS


### NOTATION



$^*$ - Asterisks indicate confirmed (or reported) cases, and all cases otherwise (or true number of cases) 

$t$ - Time since early stages of the epidemic

$\tau$   - age of infection (the time elapsed since the last infection)

$\tau'$ - Age of immunity (the time elapsed since the last recovery or vaccination)

$N$ - Total population

${\mu}$ - natural mortality rate (per day per person)

${\epsilon}$ - vaccine efficacy

${\nu}$  - yearly vaccination rate (or coverage) 

${\eta_C},{\eta_I}$ - cumulative $C$ and $I$

$\zeta$ - logarithm of $I$

$\lambda_0$ - Initial logarithmic growth rate

$R_0$ - Initial reproduction number (for COVID-19 and influenza)

$r_0$ - Initial disease-related  mortality (for COVID-19 and influenza)

$\alpha(t)$ - fraction of the reported to true  case incidence at time $t$

$\dot{C}_0,\dot{C}^*_0$ - Initial incidence

$R(t),R^*(t)$ - Basic reproduction number

$R_e(t),R^*_e(t)$ - Effective reproduction number

$R_{min}(t),R_{max}(t)$ - Min and max seasonal reproduction number  (for COVID-19 and influenza)

$R_s(t),R^*_s(t)$ - Seasonal reproduction number
$\Omega(t),\Omega^*(t)$ - current lockdown factor 

$\Omega_{rel}$ - Short-term lockdown factor relaxation value  (post-lockdown)

$\tau_{rel}$ - Short-term lockdown factor relaxation time constant  

$\Omega_{\infty}$ - Long-term lockdown factor relaxation value   (new normal)

$\theta_i$ - lockdown start/exit thresholds

$m_i(t)$ - index for control measure $i$ (e.g. stringency index or school closing)

$\eta_i(t)$ - effectiveness of control measure $i$ 

$f(t)$ - fatigue factor

$M(t)$ - outdoor mobility

$k(t)$ - outdoor temperature

$\lambda(t),\lambda^*(t)$ -  logarithmic growth rate

$T(t),T^*(t)$ - total umber of tests

$r(t),r^*(t)$ -  disease-related  mortality

$C(t),C^*(t)$ - Total cases 

$C^*_{data}(t)$ - Total cases data (as reported)

$C^*_{diag}(t)$ - Total cases data (wrt diagnosis date)

$C_{ri}(t),C_{ri}^*(t)$ - Total reinfection cases 

$H(t),H^*(t)$ - total recoveries

${D}(t),{D}^*(t)$ - deaths attributable to COVID-19 only

${D}_{\mu}(t),{D}^*_{\mu}(t)$ - deaths of the infected population which are attributable to natural mortality

${D}_{tot}(t),{D}_{tot}^*(t)$ - total deaths 

$D^*_{data}(t)$ - Deaths data (as reported)

$D^*_{diag}(t)$ - Deaths data (wrt diagnosis date)

$I(t),I^*(t)$ - Infected population at time $t$

$I_{min}$ -  lower limit on infection prevalence

$F(t),F^*(t)$ - Infectious population at time $t$

$S(t),S^*(t)$ -  susceptible population at time $t$

$\tilde{I}(t,\tau),\tilde{I}^*(t,\tau)$ - Currently infected population at time $t$ with  infection age $\tau$ 

$L(t),L^*(t)$ - Total lost disease-induced immunities (recovered and susceptible)

$J(t),J^*(t)$ - currently recovered  immune  population at time $t$ (recovered and immune)

$\tilde{J}(t,\tau'),\tilde{J}^*(t,\tau')$ - currently recovered immune population at time $t$ with  immunity age $\tau'$ 

$V(t)$ - Total vaccine-induced immunities

$V'(t)$ - Total vaccinated

$U(t)$ - Total lost vaccine-induced immunities (vaccinated and susceptible)

$K(t)$ - currently vaccinated immune  population at time $t$ (vaccinated and immune)

$\tilde{K}(t,\tau')$ - currently vaccinated immune  population at time $t$ with  immunity age $\tau'$ 

$p_{\beta}(\tau)$ - age-specific transmission rate (for COVID-19 and influenza)

$p_{\gamma}(\tau)$ - age-specific  recovery rate (for mild, severe, and critical cases)

$p_{\delta}(\tau)$ - age-specific  disease-related mortality rate

$p_{\nu}(\tau')$ - age-specific  waning immunity rate (after natural infection)

$p_{\nu'}(\tau')$ - age-specific  waning immunity rate (after vaccination)

$\Lambda(\tau),\Lambda^*(\tau)$ - probability, for an
infected individual, to remain in the infected state until infection age $\tau$ (survival or removal function)

$\Lambda_{\nu}(\tau')$ -probability, for an
infected individual, to remain in the immune state until immunity age $\tau'$

$\bar{\beta}(t),\bar{\beta}^*(t)$ -  contact rate (age-averaged model)

$\bar{\gamma}(t),\bar{\gamma}^*(t)$ -   recovery rate (age-averaged model)

$\bar{\delta}(t),\bar{\delta}^*(t)$ -  death rate (age-averaged model)

$\bar{R}(t),\bar{R}^*(t)$ -  reproduction number (age-averaged model)

$\tau_{diag}$ - mean time to diagnosis 

$\tau_{inf}$ - mean  infectious period

$\tau_{cut}$ - contact tracing cutoff on distribution $p_{\beta}$ 

$\tau_{\beta}$ - scale parameter of distribution $p_{\beta}$ 

$\tau_{\gamma}$ - scale parameter of distribution $p_{\gamma}$ 

$\tau_{\delta}$ - scale parameter of distribution $p_{\delta}$ 

$\tau_{\nu}$ - scale parameter of distribution $p_{\nu}$ 

$s_{\beta}$ - shape parameter of distribution $p_{\beta}$ 

$s_{\gamma}$ - shape parameter of distribution $p_{\gamma}$ 

$s_{\delta}$ - shape parameter of distribution $p_{\delta}$ 

$s_{\nu}$ - shape parameter of distribution $p_{\nu}$ 

$p_{asym}$  - probability of asymptomatic infection

$p_{sym}$ - probability of symptomatic infection

$p_{fev | sym}$ - probability of fever given symptoms 

$p_{sev|sym}$ - probability of severe infection given symptoms 

$p_{crit|sym}$ - probability of critical infection given symptoms 

$p_{diag | sym}$ - probability of diagnosis given symptoms 

$p_{hosp}$  - probability of hospitalization

$p_{mild}$ - probability of mild infection

$\tau_{hosp}$ - mean time to hospitalization

$\Delta_{hosp}$ - mean hospitalization duration 

$\Delta_{ICU}$ - mean duration of ICU  stay

$\Pi$ - variant multiplicative advantage

$t_{var}$ - variant appearance time

$t_{sim}$ - projection time



