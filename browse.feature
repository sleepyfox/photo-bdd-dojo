Feature: browse friend's photos
  As a friend of a photographer
  I want to see my friends' amazing photos
  So that I can dream of going to Bali one day

  Scenario: browse
      Given that my friend Bob has taken several pictures
      When I view his photo stream
      Then I should see his latest approved photo first
      And then let you scroll through them vertically
