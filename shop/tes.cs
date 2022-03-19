using System;
using DrCloud.Core.Helpers;
using DrCloud.Internal.ApiAction;
using DrCloud.Internal.ApiModel;
using DrCloud.Internal.ApiModel.ApiInputModels;
using DrCloud.Internal.ApiModel.ApiResponseModels;
using MediatR;
using Microsoft.AspNetCore.Mvc;
using System.Net;
using System.Threading.Tasks;

namespace DrCloud.Internal.API.Controllers
{
    [ApiController]
    [Route("user")]
    public class UserController : BaseController
    {
        public UserController(IMediator mediator,
            ICurrentContext currentContext
        ) : base(mediator, currentContext)
        {
        }


        /// <summary>
        /// Health check
        /// </summary>
        /// <returns></returns>
        [HttpGet]
        [Route("{userId}/get-groups")]
        [Produces("application/json")]
        [ProducesResponseType(typeof(ApiResponseModel<UserGetGroupsResponseModel>), (int)HttpStatusCode.OK)]
        public async Task<IActionResult> GetGroups([FromRoute] Guid UserId)
        {
            return await _mediator.Send(ApiActionModel.CreateRequest(new UserGetGroupsInputModel()
            {
                UserId= UserId
            }
                
                ));
        }

    }
}
