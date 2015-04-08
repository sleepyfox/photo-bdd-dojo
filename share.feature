Feature: share a photo
  As a photographer
  I want to take pictures
  So that all my friends can see what an amazing life I have

  Scenario: publish a photo
    Given that I'm logged in
    When I take an amazing photo
    And approve it (obviously)
    Then I should be able to see it on my photo stream

  Scenario: publish another photo
    Given that I'm logged in
    And that I have already published one photo
    When I take another amazing photo
    And approve it (obviously)
    Then I should be able to see the new photo on my photo stream
    And I should be able to see my previous photo on my photo stream
