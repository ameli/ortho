=====================
ortho's documentation
=====================

.. toctree::
    :maxdepth: 1
    :caption: Documentation
    :hidden:

    Home <self>
    API Reference <api>


.. |image01| replace:: $\phi_i^{\perp}$
.. |image02| replace:: $\phi_i$
.. |image03| replace:: $t \in [0,L]$
.. |image04| replace:: $w(t) = t^{-1}$
.. |image05| replace:: $\delta_{ij}$
.. |image06| replace:: $i_0$
.. |image07| replace:: $n$
.. |image08| replace:: $L$
.. |image09| replace:: $\alpha_i$
.. |image10| replace:: $a_{ij}$
.. |image11| replace:: $$\phi_i(t) = t^{\frac{1}{i+1}}, \qquad i = i_0,\dots,i_0+n.$$
.. |image12| replace:: $$\phi_i^{\perp}(t) = \alpha_i \sum_{j = i_0}^{i_0+n} a_{ij} \phi_j(t), \qquad i = i_0,\dots,i_0+n.$$
.. |image13| replace:: $$\langle \phi_i^{\perp},\phi_j^{\perp} \rangle_{L^2([0,L],\mathrm{d}t/t)} = \int_0^L \phi_i^{\perp}(t) \phi_j^{\perp}(t) \frac{\mathrm{d}t}{t} = \delta_{ij},$$

.. include:: ../../README.rst
   :start-after: .. include_after_this_line
