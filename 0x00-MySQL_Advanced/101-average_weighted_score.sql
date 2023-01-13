-- creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and stores the average weighted score for all students

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER |
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
  UPDATE users AS Us, 
    (SELECT Us.id, SUM(score * weight) / SUM(weight) AS w_avg 
    FROM users AS Us 
    JOIN corrections as C ON Us.id=C.user_id 
    JOIN projects AS Pr ON C.project_id=Pr.id 
    GROUP BY Us.id)
  AS WA
  SET Us.average_score = WA.w_avg 
  WHERE Us.id=WA.id;
END;
