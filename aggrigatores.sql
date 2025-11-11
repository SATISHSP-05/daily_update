-- Count 
SELECT Continent, COUNT(Name) AS TotalCountries
FROM country
GROUP BY Continent;

--average 
SELECT Continent, AVG(LifeExpectancy) AS AvgLifeExpectancy
FROM country
GROUP BY Continent;

--total 
SELECT Region, SUM(Population) AS TotalPopulation
FROM country
GROUP BY Region;

-- maximum
SELECT Continent, MAX(Population) AS MaxPopulation
FROM country
GROUP BY Continent;

--minimum
SELECT Continent, MIN(GNP) AS MinGNP
FROM country
GROUP BY Continent;

--group by
SELECT Continent, COUNT(Name) AS CountryCount
FROM country
GROUP BY Continent


--having
SELECT Region, SUM(Population) AS TotalPopulation
FROM country
GROUP BY Region
HAVING SUM(Population) > 100000000;

