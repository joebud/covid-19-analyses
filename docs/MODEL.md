---
output: 
  html_document: 
    theme: paper
    toc: true
    toc_float: 
      collapsed: true
    toc_depth: 3
    self_contained: yes
    mathjax: https://mathjax.rstudio.com/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML
---

 
# COVID-19 Projections

Generating COVID-19 projections for various scenarios and countries


## BRIEF MODEL DESCRIPTION


### Dynamics


$$ 
\dot{C} =  \frac{R_e}{ \tau_{inf}} F  
$$

$$ 
\dot{H} = (1-r) \int _{0}^{\infty} p_{\gamma} \tilde{I} \,d\tau 
$$

$$ 
\dot{D} = r \int _{0}^{\infty} p_{\delta} \tilde{I} \,d\tau
$$

$$ 
\dot{D}_{\mu} = \mu I
$$


$$ 
{I} = \int _{0}^{\infty} \tilde{I} \,d\tau
$$


$$ 
{F}  = \tau_{inf} \int _{0}^{\infty} p_{\beta} \tilde{I} \,d\tau
$$  

$$ 
(\partial_t+\partial_{\tau}) \tilde{I} = - p_{\gamma \delta} \tilde{I}
$$

$$ 
\dot{L} =  \int _{0}^{\infty} p_{\nu} \tilde{J} \,d\tau'
$$

$$ 
{J} = \int _{0}^{\infty} \tilde{J} \,d\tau'
$$

$$ 
(\partial_t+\partial_{\tau'}) \tilde{J} = - p_{\nu} \tilde{J}
$$

$$ 
\dot{U} =  \int _{0}^{\infty} p_{\nu} \tilde{K} \,d\tau'
$$

$$ 
{K} = \int _{0}^{\infty} \tilde{K} \,d\tau'
$$

$$ 
(\partial_t+\partial_{\tau'}) \tilde{K} = - p_{\nu} \tilde{K}
$$


$$ 
{R}_e = \frac{S}{N} R
$$



$$ 
{S} = \max(S_{min}, N-I-J-K-D)
$$


$$ 
{C} = I+H+ {D}
$$

$$ 
{H} = J+L
$$

$$ 
{V} = K+U
$$




### Initial conditions



$$ 
\tilde{I}(0,\tau) = \dot{C}_0 \Lambda(\tau) e^{-\lambda_0 \tau}
$$

$$ 
\tilde{J}(0,\tau') =  (1-r_0)  \dot{C}_0 \Lambda_{\nu}(\tau') e^{-\lambda_0 \tau'}
\int _{0}^{\infty} p_{\gamma}(\tau) e^{-\lambda_0 \tau} \,d\tau
$$

$$ 
\tilde{K}(0,\tau') =  0
$$

$$ 
\tilde{I}(t,0) = \dot{C}(t)
$$

$$ 
\tilde{J}(t,0) = \dot{H}(t)
$$

$$ 
\tilde{K}(t,0) = \dot{V}(t)
$$




<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-CTEQ2C7JBB"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-CTEQ2C7JBB');
</script> 





 
