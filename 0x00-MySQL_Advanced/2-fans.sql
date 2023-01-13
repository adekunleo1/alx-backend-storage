-- Script ranks for country origin of bands, by unique fan base
SELECT origin AS origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin 
ORDER BY nb_fans DESC;
