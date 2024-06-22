$(function() {
  $(".draggable").draggable({
      revert: "invalid"
  });

  $("#in-progress, #completed, #overdue").droppable({
      accept: ".draggable",
      drop: function(event, ui) {
          var taskId = ui.draggable.attr("id");
          var newStatus = $(this).attr("id");
          $(this).append(ui.draggable);
          updateTaskStatus(taskId, newStatus);
      }
  });

  function updateTaskStatus(taskId, newStatus) {
      $.ajax({
          url: `api/task/status/${taskId}`,
          type: 'POST',
          headers: {
              'X-CSRFToken': '{{ csrf_token }}'
          },
          data: {
              status: newStatus
          },
          success: function(response) {
              console.log('Task status updated successfully:', response);
          },
          error: function(error) {
              console.error('Error updating task status:', error);
          }
      });
  }
});